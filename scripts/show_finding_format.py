#!/usr/bin/env python3
"""
Script to show the format of a finding and how to work with it
"""
import sys
import os
import json

# Add project root directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def show_finding_format():
    """Show the complete format of a finding"""
    client = SoloditClient()
    
    print("=" * 80)
    print("FINDING FORMAT EXAMPLE")
    print("=" * 80)
    
    # Get one HIGH severity finding
    data = client.search_findings(
        page=1,
        page_size=1,
        filters={
            "impact": ["HIGH"],
            "qualityScore": 4
        }
    )
    
    if not data['findings']:
        print("No findings found")
        return
    
    finding = data['findings'][0]
    
    print("\n📋 COMPLETE FINDING STRUCTURE (JSON):")
    print("-" * 80)
    print(json.dumps(finding, indent=2, ensure_ascii=False))
    
    print("\n\n" + "=" * 80)
    print("HOW TO ACCESS FINDING DATA")
    print("=" * 80)
    
    print("\n1️⃣ BASIC INFORMATION:")
    print(f"   ID:          {finding.get('id')}")
    print(f"   Title:       {finding.get('title')}")
    print(f"   Impact:      {finding.get('impact')}")
    print(f"   Quality:     {finding.get('quality_score')}/5")
    print(f"   Rarity:      {finding.get('general_score')}/5")
    
    print("\n2️⃣ AUDIT FIRM:")
    print(f"   Firm Name:   {finding.get('firm_name')}")
    print(f"   Firm ID:     {finding.get('auditfirm_id')}")
    print(f"   Firm Logo:   {finding.get('firm_logo_square')}")
    
    print("\n3️⃣ PROTOCOL:")
    print(f"   Protocol:    {finding.get('protocol_name')}")
    print(f"   Protocol ID: {finding.get('protocol_id')}")
    
    print("\n4️⃣ CONTENT:")
    content = finding.get('content', '')
    print(f"   Content Length: {len(content)} characters")
    print(f"   First 200 chars: {content[:200]}...")
    print(f"   Summary: {finding.get('summary')}")
    
    print("\n5️⃣ LINKS:")
    print(f"   Source Link:  {finding.get('source_link')}")
    print(f"   GitHub Link:  {finding.get('github_link')}")
    print(f"   PDF Link:     {finding.get('pdf_link')}")
    
    print("\n6️⃣ DATES:")
    print(f"   Report Date:  {finding.get('report_date')}")
    
    print("\n7️⃣ FINDERS (Auditors):")
    finders = finding.get('issues_issue_finders', [])
    print(f"   Total Finders: {finding.get('finders_count', 0)}")
    for i, finder in enumerate(finders[:3], 1):
        handle = finder.get('wardens_warden', {}).get('handle', 'N/A')
        print(f"   {i}. {handle}")
    
    print("\n8️⃣ TAGS:")
    tags = finding.get('issues_issuetagscore', [])
    print(f"   Total Tags: {len(tags)}")
    for i, tag in enumerate(tags[:5], 1):
        tag_title = tag.get('tags_tag', {}).get('title', 'N/A')
        print(f"   {i}. {tag_title}")
    
    print("\n9️⃣ CONTEST INFO (if applicable):")
    print(f"   Contest ID:    {finding.get('contest_id')}")
    print(f"   Contest Link:  {finding.get('contest_link')}")
    print(f"   Prize:         {finding.get('contest_prize_txt')}")
    print(f"   Sponsor:       {finding.get('sponsor_name')}")
    
    print("\n\n" + "=" * 80)
    print("PYTHON CODE EXAMPLES")
    print("=" * 80)
    
    print("""
# Example 1: Get basic info
finding = data['findings'][0]
title = finding['title']
impact = finding['impact']
quality = finding['quality_score']

# Example 2: Get full content (markdown)
content = finding['content']
print(content)  # Full vulnerability description

# Example 3: Get all tags
tags = [tag['tags_tag']['title'] for tag in finding.get('issues_issuetagscore', [])]
print(tags)  # ['Reentrancy', 'Access Control', ...]

# Example 4: Get all finders
finders = [f['wardens_warden']['handle'] for f in finding.get('issues_issue_finders', [])]
print(finders)  # ['auditor1', 'auditor2', ...]

# Example 5: Check if has PDF
has_pdf = finding.get('pdf_link') is not None

# Example 6: Get protocol categories
protocol = finding.get('protocols_protocol', {})
categories = protocol.get('protocols_protocolcategoryscore', [])
for cat in categories:
    category_name = cat['protocols_protocolcategory']['title']
    score = cat['score']
    print(f"{category_name}: {score}")
""")
    
    print("\n" + "=" * 80)
    print("RESPONSE STRUCTURE")
    print("=" * 80)
    
    print("""
The API returns:
{
    "findings": [
        { ... finding object ... },
        { ... finding object ... },
        ...
    ],
    "metadata": {
        "totalResults": 8022,
        "currentPage": 1,
        "pageSize": 50,
        "totalPages": 161,
        "elapsed": 0.234
    },
    "rateLimit": {
        "limit": 20,
        "remaining": 19,
        "reset": 1234567890
    }
}
""")


def show_practical_example():
    """Show practical example of working with findings"""
    print("\n\n" + "=" * 80)
    print("PRACTICAL EXAMPLE: Extract and Save Finding")
    print("=" * 80)
    
    client = SoloditClient()
    
    # Search for reentrancy findings
    data = client.search_findings(
        page=1,
        page_size=3,
        filters={
            "keywords": "reentrancy",
            "impact": ["HIGH"],
            "qualityScore": 4
        }
    )
    
    print(f"\nFound {data['metadata']['totalResults']} HIGH quality reentrancy findings")
    print("\nProcessing first 3 findings:\n")
    
    for i, finding in enumerate(data['findings'], 1):
        print(f"{i}. {finding['title']}")
        print(f"   Firm: {finding.get('firm_name', 'N/A')}")
        print(f"   Protocol: {finding.get('protocol_name', 'N/A')}")
        print(f"   Quality: {finding['quality_score']}/5")
        print(f"   Link: {finding.get('source_link', 'N/A')}")
        
        # Get tags
        tags = [tag['tags_tag']['title'] for tag in finding.get('issues_issuetagscore', [])]
        print(f"   Tags: {', '.join(tags[:3])}")
        
        # Get content preview
        content = finding.get('content', '')
        if content:
            print(f"   Content preview: {content[:100]}...")
        
        print()


if __name__ == "__main__":
    try:
        show_finding_format()
        show_practical_example()
    except Exception as e:
        print(f"❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
