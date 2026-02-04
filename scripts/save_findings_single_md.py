#!/usr/bin/env python3
"""
Script to save all findings to a SINGLE markdown file
Usage: python scripts/save_findings_single_md.py [keyword] [count]
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def save_findings_to_single_file(keyword=None, count=10, impact=None, output_file=None):
    """Search and save all findings to a single markdown file"""
    
    client = SoloditClient()
    
    print("=" * 80)
    print("SAVE ALL FINDINGS TO SINGLE MARKDOWN FILE")
    print("=" * 80)
    
    # Prepare filters
    filters = {}
    if keyword:
        filters['keywords'] = keyword
        print(f"\n🔍 Searching for: '{keyword}'")
    
    if impact:
        filters['impact'] = impact
        print(f"📊 Impact filter: {', '.join(impact)}")
    
    # Search
    print(f"📄 Requesting {count} findings...\n")
    
    data = client.search_findings(
        page=1,
        page_size=count,
        filters=filters if filters else None
    )
    
    total = data['metadata']['totalResults']
    findings = data['findings']
    
    print(f"✅ Found {total} total findings")
    print(f"📥 Saving {len(findings)} findings to single file...\n")
    
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
    content.append("## Report Information\n\n")
    if keyword:
        content.append(f"**Search Query:** `{keyword}`\n\n")
    content.append(f"**Total Found:** {total} findings\n\n")
    content.append(f"**Included:** {len(findings)} findings\n\n")
    content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    # Statistics
    impact_counts = {}
    quality_sum = 0
    for finding in findings:
        impact = finding['impact']
        impact_counts[impact] = impact_counts.get(impact, 0) + 1
        quality_sum += finding.get('quality_score', 0)
    
    avg_quality = quality_sum / len(findings) if findings else 0
    
    content.append("## Statistics\n\n")
    content.append(f"**Average Quality Score:** {avg_quality:.2f}/5\n\n")
    content.append("**By Impact Level:**\n\n")
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
        impact = finding['impact']
        anchor = f"finding-{i}"
        content.append(f"{i}. [{impact}] [{title}](#{anchor})\n")
    
    content.append("\n---\n\n")
    
    # Findings
    for i, finding in enumerate(findings, 1):
        print(f"  {i:2d}. [{finding['impact']}] {finding['title'][:60]}...")
        
        # Finding header
        content.append(f"## Finding #{i}: {finding['title']} {{#finding-{i}}}\n\n")
        
        # Metadata table
        content.append("| Property | Value |\n")
        content.append("|----------|-------|\n")
        content.append(f"| **Impact** | {finding.get('impact', 'N/A')} |\n")
        content.append(f"| **Quality Score** | {finding.get('quality_score', 0)}/5 |\n")
        content.append(f"| **Audit Firm** | {finding.get('firm_name', 'N/A')} |\n")
        content.append(f"| **Protocol** | {finding.get('protocol_name', 'N/A')} |\n")
        
        # Report date
        report_date = finding.get('report_date')
        if report_date:
            content.append(f"| **Report Date** | {report_date} |\n")
        
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
        
        # Main content (without extra header since content already has its own structure)
        finding_content = finding.get('content', '')
        if finding_content:
            content.append(finding_content)
            content.append("\n\n")
        else:
            content.append("*No detailed description available.*\n\n")
        
        # Separator
        content.append("---\n\n")
    
    # Footer
    content.append("## End of Report\n\n")
    content.append(f"**Total Findings:** {len(findings)}\n\n")
    content.append(f"**Generated by:** Solodit API Client\n\n")
    content.append(f"**Timestamp:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    # Write to file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(''.join(content))
    
    print(f"\n{'='*80}")
    print(f"✅ Successfully saved {len(findings)} findings!")
    print(f"📄 Output file: {output_file}")
    print(f"📊 File size: {os.path.getsize(output_file) / 1024:.1f} KB")
    print(f"{'='*80}")
    
    return output_file


def main():
    """Main function"""
    
    # Parse arguments
    keyword = None
    count = 10
    impact = None
    output_file = None
    
    if len(sys.argv) > 1:
        keyword = sys.argv[1]
    
    if len(sys.argv) > 2:
        try:
            count = int(sys.argv[2])
            count = min(count, 100)  # Max 100
        except ValueError:
            print(f"Warning: Invalid count '{sys.argv[2]}', using default 10")
            count = 10
    
    if len(sys.argv) > 3:
        impact_arg = sys.argv[3].upper()
        if impact_arg in ['HIGH', 'MEDIUM', 'LOW', 'GAS']:
            impact = [impact_arg]
        else:
            print(f"Warning: Invalid impact '{sys.argv[3]}', ignoring")
    
    if len(sys.argv) > 4:
        output_file = sys.argv[4]
    
    try:
        output_file = save_findings_to_single_file(keyword, count, impact, output_file)
        
        print(f"\n💡 Tip: Open {output_file} in your markdown viewer")
        print(f"💡 Or convert to PDF: pandoc {output_file} -o report.pdf")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("""
Usage: python scripts/save_findings_single_md.py [keyword] [count] [impact] [output_file]

Arguments:
  keyword       Search keyword (optional)
  count         Number of findings to save (default: 10, max: 100)
  impact        Filter by impact: HIGH, MEDIUM, LOW, GAS (optional)
  output_file   Output filename (optional, auto-generated if not specified)

Examples:
  # Save 10 findings to auto-generated file
  python scripts/save_findings_single_md.py

  # Save reentrancy findings
  python scripts/save_findings_single_md.py reentrancy

  # Save 20 reentrancy findings
  python scripts/save_findings_single_md.py reentrancy 20

  # Save 15 HIGH severity oracle findings
  python scripts/save_findings_single_md.py oracle 15 HIGH

  # Save to specific file
  python scripts/save_findings_single_md.py supportsInterface 10 HIGH my_report.md

  # Multi-word keywords
  python scripts/save_findings_single_md.py "flash loan" 10

Output:
  - Single markdown file with all findings
  - Table of contents with links
  - Statistics and metadata
  - Full descriptions for each finding
        """)
        sys.exit(0)
    
    main()
