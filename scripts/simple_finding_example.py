#!/usr/bin/env python3
"""
Simple example showing how to work with findings
"""
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def main():
    client = SoloditClient()
    
    print("=" * 80)
    print("SIMPLE FINDING EXAMPLE")
    print("=" * 80)
    
    # Search for findings
    data = client.search_findings(
        page=1,
        page_size=3,
        filters={"keywords": "reentrancy", "impact": ["HIGH"]}
    )
    
    print(f"\n✅ Found {data['metadata']['totalResults']} findings\n")
    
    # Process each finding
    for i, finding in enumerate(data['findings'], 1):
        print(f"\n{'='*80}")
        print(f"FINDING #{i}")
        print('='*80)
        
        # 1. Basic Info
        print(f"\n📌 BASIC INFO:")
        print(f"   Title:    {finding['title']}")
        print(f"   Impact:   {finding['impact']}")
        print(f"   Quality:  {finding['quality_score']}/5")
        print(f"   Rarity:   {finding['general_score']}/5")
        
        # 2. Source
        print(f"\n🏢 SOURCE:")
        print(f"   Firm:     {finding.get('firm_name', 'N/A')}")
        print(f"   Protocol: {finding.get('protocol_name', 'N/A')}")
        
        # 3. Links
        print(f"\n🔗 LINKS:")
        print(f"   Source:   {finding.get('source_link', 'N/A')}")
        
        # 4. Content (Markdown format)
        content = finding.get('content', '')
        print(f"\n📄 CONTENT:")
        print(f"   Length:   {len(content)} characters")
        print(f"   Format:   {finding.get('kind', 'N/A')}")  # Usually "MARKDOWN"
        if content:
            print(f"\n   Preview:")
            print("   " + "-" * 76)
            # Show first 300 characters
            preview = content[:300].replace('\n', '\n   ')
            print(f"   {preview}...")
            print("   " + "-" * 76)
        
        # 5. Tags
        tags = finding.get('issues_issuetagscore', [])
        if tags:
            print(f"\n🏷️  TAGS:")
            tag_names = [tag['tags_tag']['title'] for tag in tags]
            print(f"   {', '.join(tag_names)}")
        
        # 6. Finders
        finders = finding.get('issues_issue_finders', [])
        if finders:
            print(f"\n👥 FINDERS ({finding.get('finders_count', 0)}):")
            for finder in finders[:3]:
                handle = finder['wardens_warden']['handle']
                print(f"   - {handle}")
    
    print("\n\n" + "=" * 80)
    print("HOW TO USE THE DATA")
    print("=" * 80)
    
    print("""
# Get the response
data = client.search_findings(page=1, page_size=10)

# Access findings list
findings = data['findings']

# Work with first finding
finding = findings[0]

# Get title and content
title = finding['title']
content = finding['content']  # Full markdown text

# Get metadata
impact = finding['impact']  # "HIGH", "MEDIUM", "LOW", "GAS"
quality = finding['quality_score']  # 0-5
firm = finding.get('firm_name')
protocol = finding.get('protocol_name')

# Get link to original source
link = finding.get('source_link')

# Get all tags
tags = [tag['tags_tag']['title'] for tag in finding.get('issues_issuetagscore', [])]

# Get all finders/auditors
finders = [f['wardens_warden']['handle'] for f in finding.get('issues_issue_finders', [])]

# Save to file
with open('finding.md', 'w') as f:
    f.write(f"# {title}\\n\\n")
    f.write(f"**Impact:** {impact}\\n")
    f.write(f"**Quality:** {quality}/5\\n")
    f.write(f"**Firm:** {firm}\\n\\n")
    f.write(content)
""")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)
