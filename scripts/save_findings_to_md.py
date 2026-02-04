#!/usr/bin/env python3
"""
Script to save findings to markdown files
Usage: python scripts/save_findings_to_md.py [keyword] [count]
"""
import sys
import os
from datetime import datetime

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def sanitize_filename(text):
    """Convert text to safe filename"""
    # Remove or replace unsafe characters
    unsafe_chars = '<>:"/\\|?*'
    for char in unsafe_chars:
        text = text.replace(char, '_')
    # Limit length
    return text[:100]


def save_finding_to_md(finding, index, output_dir="findings"):
    """Save single finding to markdown file"""
    
    # Create output directory if not exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Generate filename
    title = finding.get('title', 'Untitled')
    safe_title = sanitize_filename(title)
    filename = f"{index:02d}_{safe_title}.md"
    filepath = os.path.join(output_dir, filename)
    
    # Prepare content
    content = []
    
    # Header
    content.append(f"# {title}\n")
    content.append("---\n")
    
    # Metadata
    content.append("## Metadata\n")
    content.append(f"- **Impact:** {finding.get('impact', 'N/A')}\n")
    content.append(f"- **Quality Score:** {finding.get('quality_score', 0)}/5\n")
    content.append(f"- **Rarity Score:** {finding.get('general_score', 0)}/5\n")
    content.append(f"- **Audit Firm:** {finding.get('firm_name', 'N/A')}\n")
    content.append(f"- **Protocol:** {finding.get('protocol_name', 'N/A')}\n")
    
    # Report date
    report_date = finding.get('report_date')
    if report_date:
        content.append(f"- **Report Date:** {report_date}\n")
    
    # Links
    source_link = finding.get('source_link')
    if source_link:
        content.append(f"- **Source:** [{source_link}]({source_link})\n")
    
    github_link = finding.get('github_link')
    if github_link:
        content.append(f"- **GitHub:** [{github_link}]({github_link})\n")
    
    pdf_link = finding.get('pdf_link')
    if pdf_link:
        content.append(f"- **PDF:** [{pdf_link}]({pdf_link})\n")
    
    content.append("\n")
    
    # Tags
    tags = finding.get('issues_issuetagscore', [])
    if tags:
        content.append("## Tags\n")
        tag_names = [tag['tags_tag']['title'] for tag in tags]
        content.append(", ".join(f"`{tag}`" for tag in tag_names))
        content.append("\n\n")
    
    # Finders
    finders = finding.get('issues_issue_finders', [])
    if finders:
        content.append("## Found By\n")
        for finder in finders:
            handle = finder['wardens_warden']['handle']
            content.append(f"- {handle}\n")
        content.append("\n")
    
    # Main content
    content.append("---\n\n")
    content.append("## Description\n\n")
    
    finding_content = finding.get('content', '')
    if finding_content:
        content.append(finding_content)
    else:
        content.append("*No detailed description available.*\n")
    
    # Summary
    summary = finding.get('summary')
    if summary:
        content.append("\n\n---\n\n")
        content.append("## Summary\n\n")
        content.append(summary)
    
    # Write to file
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(''.join(content))
    
    return filepath


def save_findings(keyword=None, count=10, impact=None):
    """Search and save findings to markdown files"""
    
    client = SoloditClient()
    
    print("=" * 80)
    print("SAVE FINDINGS TO MARKDOWN FILES")
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
    print(f"📥 Saving {len(findings)} findings to markdown files...\n")
    
    # Create output directory with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    if keyword:
        output_dir = f"findings_{sanitize_filename(keyword)}_{timestamp}"
    else:
        output_dir = f"findings_{timestamp}"
    
    # Save each finding
    saved_files = []
    for i, finding in enumerate(findings, 1):
        filepath = save_finding_to_md(finding, i, output_dir)
        saved_files.append(filepath)
        
        title = finding['title'][:60]
        impact = finding['impact']
        quality = finding['quality_score']
        
        print(f"{i:2d}. [{impact}] {title}... → {filepath}")
    
    # Create index file
    index_path = os.path.join(output_dir, "INDEX.md")
    create_index_file(findings, index_path, keyword, total)
    
    print(f"\n{'='*80}")
    print(f"✅ Successfully saved {len(saved_files)} findings!")
    print(f"📁 Output directory: {output_dir}/")
    print(f"📋 Index file: {index_path}")
    print(f"{'='*80}")
    
    return output_dir


def create_index_file(findings, filepath, keyword, total):
    """Create index file with all findings"""
    
    content = []
    
    # Header
    content.append("# Findings Index\n\n")
    
    if keyword:
        content.append(f"**Search keyword:** `{keyword}`\n\n")
    
    content.append(f"**Total found:** {total} findings\n")
    content.append(f"**Saved:** {len(findings)} findings\n")
    content.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
    
    content.append("---\n\n")
    
    # Statistics
    impact_counts = {}
    for finding in findings:
        impact = finding['impact']
        impact_counts[impact] = impact_counts.get(impact, 0) + 1
    
    content.append("## Statistics\n\n")
    for impact in ['HIGH', 'MEDIUM', 'LOW', 'GAS']:
        count = impact_counts.get(impact, 0)
        if count > 0:
            content.append(f"- **{impact}:** {count}\n")
    
    content.append("\n---\n\n")
    
    # List of findings
    content.append("## Findings\n\n")
    
    for i, finding in enumerate(findings, 1):
        title = finding['title']
        impact = finding['impact']
        quality = finding['quality_score']
        firm = finding.get('firm_name', 'N/A')
        
        safe_title = sanitize_filename(title)
        filename = f"{i:02d}_{safe_title}.md"
        
        content.append(f"### {i}. [{impact}] {title}\n\n")
        content.append(f"- **Quality:** {quality}/5\n")
        content.append(f"- **Firm:** {firm}\n")
        content.append(f"- **File:** [{filename}]({filename})\n\n")
    
    # Write index
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(''.join(content))


def main():
    """Main function"""
    
    # Parse arguments
    keyword = None
    count = 10
    impact = None
    
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
    
    try:
        output_dir = save_findings(keyword, count, impact)
        
        print(f"\n💡 Tip: Open {output_dir}/INDEX.md to see all findings")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ['-h', '--help']:
        print("""
Usage: python scripts/save_findings_to_md.py [keyword] [count] [impact]

Arguments:
  keyword    Search keyword (optional)
  count      Number of findings to save (default: 10, max: 100)
  impact     Filter by impact: HIGH, MEDIUM, LOW, GAS (optional)

Examples:
  python scripts/save_findings_to_md.py
  python scripts/save_findings_to_md.py reentrancy
  python scripts/save_findings_to_md.py reentrancy 20
  python scripts/save_findings_to_md.py oracle 15 HIGH
  python scripts/save_findings_to_md.py "flash loan" 10
        """)
        sys.exit(0)
    
    main()
