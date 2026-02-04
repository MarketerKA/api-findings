"""
Basic examples of using Solodit API Client
"""
import sys
import os

# Add project root directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def example_basic_search():
    """Basic search"""
    print("=" * 60)
    print("EXAMPLE 1: Basic Search")
    print("=" * 60)
    
    client = SoloditClient()
    data = client.search_findings(page=1, page_size=5)
    
    print(f"Total found: {data['metadata']['totalResults']}")
    print(f"Execution time: {data['metadata']['elapsed']:.3f}s\n")
    
    for i, finding in enumerate(data['findings'], 1):
        print(f"{i}. [{finding['impact']}] {finding['title']}")
        print(f"   Firm: {finding.get('firm_name', 'N/A')}")
        print(f"   Protocol: {finding.get('protocol_name', 'N/A')}")
        print(f"   Quality: {finding['quality_score']}/5")
        if finding.get('source_link'):
            print(f"   Link: {finding['source_link']}")
        print()


def example_high_severity():
    """Search for critical vulnerabilities"""
    print("=" * 60)
    print("EXAMPLE 2: Critical Vulnerabilities (HIGH)")
    print("=" * 60)
    
    client = SoloditClient()
    data = client.get_high_severity_findings(page=1, page_size=5)
    
    print(f"Found HIGH severity: {data['metadata']['totalResults']}\n")
    
    for finding in data['findings']:
        print(f"[HIGH] {finding['title']}")
        print(f"  Firm: {finding.get('firm_name', 'N/A')}")
        print(f"  Quality: {finding['quality_score']}/5")
        print()


def example_search_by_keyword():
    """Search by keywords"""
    print("=" * 60)
    print("EXAMPLE 3: Search by keyword 'reentrancy'")
    print("=" * 60)
    
    client = SoloditClient()
    data = client.search_findings(
        page=1,
        page_size=5,
        filters={
            "keywords": "reentrancy",
            "impact": ["HIGH", "MEDIUM"],
            "sortField": "Quality",
            "sortDirection": "Desc"
        }
    )
    
    print(f"Found: {data['metadata']['totalResults']}\n")
    
    for finding in data['findings']:
        print(f"[{finding['impact']}] {finding['title']}")
        print(f"  Quality: {finding['quality_score']}/5")
        print(f"  Rarity: {finding['general_score']}/5")
        print()


if __name__ == "__main__":
    try:
        example_basic_search()
        print("\n")
        
        example_high_severity()
        print("\n")
        
        example_search_by_keyword()
        
    except Exception as e:
        print(f"Error: {e}")
