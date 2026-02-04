#!/usr/bin/env python3
"""
Universal script to export findings to markdown
Usage: python scripts/export_findings.py <keyword> [count|max] [impact]
"""
import sys
import os
import re
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def clean_content(content):
    """Remove Summary and PoC sections from content"""
    if not content:
        return content
    
    # Remove Summary section (various formats)
    content = re.sub(r'##\s+Summary\s*\n.*?(?=\n##|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'###\s+Summary\s*\n.*?(?=\n##|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove Proof of Concept / PoC sections (various formats)
    content = re.sub(r'##\s+Proof\s+of\s+Concept.*?\n.*?(?=\n##|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'###\s+Proof\s+of\s+Concept.*?\n.*?(?=\n##|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'\*\*Proof\s+of\s+Concept.*?\*\*.*?(?=\n##|\n\*\*|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'##\s+PoC\s*\n.*?(?=\n##|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    content = re.sub(r'###\s+PoC\s*\n.*?(?=\n##|\Z)', '', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Remove lines that start with "PoC:" or similar
    content = re.sub(r'^.*?PoC.*?:.*$', '', content, flags=re.MULTILINE | re.IGNORECASE)
    
    # Remove very long code blocks (likely PoC)
    def replace_long_code(match):
        code = match.group(0)
        lines = code.count('\n')
        # If code block is longer than 40 lines, remove it
        if lines > 40:
            return '\n*[Long code block removed]*\n'
        return code
    
    content = re.sub(r'```[\s\S]*?```', replace_long_code, content)
    
    # Clean up multiple empty lines
    content = re.sub(r'\n{3,}', '\n\n', content)
    
    return content.strip()


def export_findings(keyword=None, count='10', impact=None, output_file=None):
    """Export findings to markdown file"""
    
    client = SoloditClient()
    
    print("=" * 80)
    print("EXPORT FINDINGS TO MARKDOWN")
    print("=" * 80)
    
    # Prepare filters
    filters = {}
    if keyword:
        filters['keywords'] = keyword
        print(f"\n🔍 Keyword: '{keyword}'")
    
    if impact:
        filters['impact'] = impact
        print(f"📊 Impact: {', '.join(impact)}")
    
    # Determine count
    is_max = (count.lower() == 'max')
    
    if is_max:
        # First, get total count
        print(f"📄 Fetching maximum available findings...")
        test_data = client.search_findings(page=1, page_size=1, filters=filters if filters else None)
        total = test_data['metadata']['totalResults']
        count_num = min(total, 100)  # API max is 100
        print(f"✅ Found {total} total, fetching {count_num} (API limit: 100)")
    else:
        try:
            count_num = int(count)
            count_num = min(count_num, 100)
        except ValueError:
            print(f"⚠️  Invalid count '{count}', using 10")
            count_num = 10
    
    # Fetch findings
    print(f"📥 Fetching {count_num} findings...\n")
    
    data = client.search_findings(
        page=1,
        page_size=count_num,
        filters=filters if filters else None
    )
    
    total = data['metadata']['totalResults']
    findings = data['findings']
    
    print(f"✅ Total available: {total}")
    print(f"📥 Exporting: {len(findings)} findings\n")
    
    # Generate filename
    if output_file is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if keyword:
            safe_keyword = keyword.replace(' ', '_').replace('/', '_')[:30]
            output_file = f"findings_{safe_keyword}_{timestamp}.md"
        else:
            output_file = f"findings_{timestamp}.md"
    
    # Create content
    content = []
    
    # Header
    content.append("# Security Findings Report\n\n")
    
    # Metadata
    if keyword:
        content.append(f"**Search Query:** `{keyword}`\n\n")
    content.append(f"**Total Found:** {total} findings\n\n")
    content.append(f"**Exported:** {len(findings)} findings\n\n")
    content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    # Statistics
    impact_counts = {}
    quality_sum = 0
    for finding in findings:
        impact_val = finding['impact']
        impact_counts[impact_val] = impact_counts.get(impact_val, 0) + 1
        quality_sum += finding.get('quality_score', 0)
    
    avg_quality = quality_sum / len(findings) if findings else 0
    
    content.append("## Statistics\n\n")
    content.append(f"**Average Quality:** {avg_quality:.2f}/5\n\n")
    for impact_level in ['HIGH', 'MEDIUM', 'LOW', 'GAS']:
        count_val = impact_counts.get(impact_level, 0)
        if count_val > 0:
            percentage = (count_val / len(findings)) * 100
            content.append(f"- **{impact_level}:** {count_val} ({percentage:.1f}%)\n")
    
    content.append("\n---\n\n")
    
    # Table of Contents
    content.append("## Table of Contents\n\n")
    for i, finding in enumerate(findings, 1):
        title = finding['title']
        impact_val = finding['impact']
        anchor = f"finding-{i}"
        content.append(f"{i}. [{impact_val}] [{title}](#{anchor})\n")
    
    content.append("\n---\n\n")
    
    # Findings
    for i, finding in enumerate(findings, 1):
        title = finding['title'][:70]
        print(f"  {i:3d}. [{finding['impact']}] {title}...")
        
        # Finding header
        content.append(f"## Finding #{i}: {finding['title']} {{#finding-{i}}}\n\n")
        
        # Metadata table
        content.append("| Property | Value |\n")
        content.append("|----------|-------|\n")
        content.append(f"| **Impact** | {finding.get('impact', 'N/A')} |\n")
        content.append(f"| **Quality** | {finding.get('quality_score', 0)}/5 |\n")
        content.append(f"| **Firm** | {finding.get('firm_name', 'N/A')} |\n")
        content.append(f"| **Protocol** | {finding.get('protocol_name', 'N/A')} |\n")
        
        # Links
        links = []
        if finding.get('source_link'):
            links.append(f"[Source]({finding['source_link']})")
        if finding.get('github_link'):
            links.append(f"[GitHub]({finding['github_link']})")
        if finding.get('pdf_link'):
            links.append(f"[PDF]({finding['pdf_link']})")
        
        if links:
            content.append(f"| **Links** | {' · '.join(links)} |\n")
        
        content.append("\n")
        
        # Tags
        tags = finding.get('issues_issuetagscore', [])
        if tags:
            tag_names = [tag['tags_tag']['title'] for tag in tags]
            content.append(f"**Tags:** {', '.join(f'`{tag}`' for tag in tag_names)}\n\n")
        
        # Finders
        finders = finding.get('issues_issue_finders', [])
        if finders:
            finder_names = [f['wardens_warden']['handle'] for f in finders]
            content.append(f"**Found by:** {', '.join(finder_names)}\n\n")
        
        content.append("---\n\n")
        
        # Main content (cleaned)
        finding_content = finding.get('content', '')
        if finding_content:
            cleaned = clean_content(finding_content)
            if cleaned:
                content.append(cleaned)
                content.append("\n\n")
            else:
                content.append("*No description available.*\n\n")
        else:
            content.append("*No description available.*\n\n")
        
        # Separator
        content.append("---\n\n")
    
    # Footer
    content.append("## End of Report\n\n")
    content.append(f"**Total Findings:** {len(findings)}\n\n")
    content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(content))
    
    file_size = os.path.getsize(output_file) / 1024
    
    print(f"\n{'='*80}")
    print(f"✅ Successfully exported {len(findings)} findings!")
    print(f"📄 File: {output_file}")
    print(f"📊 Size: {file_size:.1f} KB")
    print(f"{'='*80}")
    
    return output_file


def main():
    """Main function"""
    
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("""
Universal Findings Export Script

Usage: python scripts/export_findings.py <keyword> [count|max] [impact] [output]

Arguments:
  keyword    Search keyword (required)
  count      Number of findings OR 'max' for maximum available (default: 10)
  impact     Filter by impact: HIGH, MEDIUM, LOW, GAS (optional)
  output     Output filename (optional, auto-generated if not specified)

Examples:
  # Export 10 findings
  python scripts/export_findings.py supportsInterface

  # Export 50 findings
  python scripts/export_findings.py reentrancy 50

  # Export ALL available findings (up to 100)
  python scripts/export_findings.py Governor max

  # Export max HIGH severity findings
  python scripts/export_findings.py oracle max HIGH

  # Export to specific file
  python scripts/export_findings.py "flash loan" 20 HIGH report.md

Features:
  • Automatically removes Summary sections
  • Automatically removes PoC (Proof of Concept) sections
  • Removes long code blocks (>50 lines)
  • Clean, professional format
  • Table of contents with links
  • Statistics included
  • Use 'max' to get all available findings (API limit: 100)
        """)
        sys.exit(0)
    
    # Parse arguments
    if len(sys.argv) < 2:
        print("Error: Keyword required")
        print("Usage: python scripts/export_findings.py <keyword> [count|max] [impact] [output]")
        print("Use --help for more information")
        sys.exit(1)
    
    keyword = sys.argv[1]
    count = sys.argv[2] if len(sys.argv) > 2 else '10'
    impact = None
    output_file = None
    
    # Parse remaining arguments
    for i in range(3, len(sys.argv)):
        arg = sys.argv[i]
        if arg.upper() in ['HIGH', 'MEDIUM', 'LOW', 'GAS']:
            impact = [arg.upper()]
        elif arg.endswith('.md'):
            output_file = arg
    
    try:
        output_file = export_findings(keyword, count, impact, output_file)
        
        print(f"\n💡 Tip: Open {output_file} in your markdown viewer")
        print(f"💡 Convert to PDF: pandoc {output_file} -o report.pdf")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
