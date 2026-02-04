"""
Advanced examples of using Solodit API Client
"""
import sys
import os

# Add project root directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def example_search_by_firm():
    """Search by audit firms"""
    print("=" * 60)
    print("EXAMPLE: Search by firms (Cyfrin, Sherlock)")
    print("=" * 60)
    
    client = SoloditClient()
    data = client.search_by_firm(
        firms=["Cyfrin", "Sherlock"],
        page=1,
        page_size=5
    )
    
    print(f"Found: {data['metadata']['totalResults']}\n")
    
    for finding in data['findings']:
        print(f"[{finding['impact']}] {finding['title']}")
        print(f"  Firm: {finding.get('firm_name', 'N/A')}")
        print()


def example_search_by_tags():
    """Search by tags"""
    print("=" * 60)
    print("EXAMPLE: Search by tags (Oracle)")
    print("=" * 60)
    
    client = SoloditClient()
    data = client.search_by_tags(
        tags=["Oracle"],
        impact=["HIGH"],
        page=1,
        page_size=5
    )
    
    print(f"Found: {data['metadata']['totalResults']}\n")
    
    for finding in data['findings']:
        print(f"[{finding['impact']}] {finding['title']}")
        tags = [t['tags_tag']['title'] for t in finding.get('issues_issuetagscore', [])]
        print(f"  Tags: {', '.join(tags[:5])}")
        print()


def example_recent_findings():
    """Recent findings"""
    print("=" * 60)
    print("EXAMPLE: Recent findings (last 30 days)")
    print("=" * 60)
    
    client = SoloditClient()
    data = client.get_recent_findings(days=30, page=1, page_size=5)
    
    print(f"Found: {data['metadata']['totalResults']}\n")
    
    for finding in data['findings']:
        print(f"[{finding['impact']}] {finding['title']}")
        print(f"  Date: {finding.get('report_date', 'N/A')}")
        print(f"  Firm: {finding.get('firm_name', 'N/A')}")
        print()


def example_advanced_filters():
    """Advanced filters"""
    print("=" * 60)
    print("EXAMPLE: Advanced Filters")
    print("=" * 60)
    
    client = SoloditClient()
    data = client.search_findings(
        page=1,
        page_size=5,
        filters={
            "impact": ["HIGH"],
            "qualityScore": 3,
            "rarityScore": 2,
            "languages": [{"value": "Solidity"}],
            "sortField": "Quality",
            "sortDirection": "Desc"
        }
    )
    
    print(f"Found: {data['metadata']['totalResults']}\n")
    
    for finding in data['findings']:
        print(f"[{finding['impact']}] {finding['title']}")
        print(f"  Quality: {finding['quality_score']}/5")
        print(f"  Rarity: {finding['general_score']}/5")
        print(f"  Protocol: {finding.get('protocol_name', 'N/A')}")
        print()


if __name__ == "__main__":
    try:
        example_search_by_firm()
        print("\n")
        
        example_search_by_tags()
        print("\n")
        
        example_recent_findings()
        print("\n")
        
        example_advanced_filters()
        
    except Exception as e:
        print(f"Error: {e}")
