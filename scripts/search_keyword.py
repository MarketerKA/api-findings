#!/usr/bin/env python3
"""
Script for searching findings by keyword
Usage: python scripts/search_keyword.py <keyword>
"""
import sys
import os

# Add project root directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def search_by_keyword(keyword: str, show_details: bool = True):
    """Search by keyword"""
    client = SoloditClient()
    
    print(f"🔍 Searching for keyword: '{keyword}'")
    print("=" * 60)
    
    # Basic search
    data = client.search_findings(
        page=1,
        page_size=10,
        filters={"keywords": keyword}
    )
    
    total = data['metadata']['totalResults']
    print(f"\n✅ Total found: {total} findings\n")
    
    if show_details and data['findings']:
        print("📋 First 10 results:")
        print("-" * 60)
        for i, finding in enumerate(data['findings'], 1):
            print(f"{i}. [{finding['impact']}] {finding['title']}")
            print(f"   Firm: {finding.get('firm_name', 'N/A')}")
            print(f"   Protocol: {finding.get('protocol_name', 'N/A')}")
            print(f"   Quality: {finding['quality_score']}/5")
            print()
    
    # Statistics by severity levels
    print("\n📊 Statistics by severity level:")
    print("-" * 60)
    
    for impact_level in ["HIGH", "MEDIUM", "LOW", "GAS"]:
        impact_data = client.search_findings(
            page=1,
            page_size=1,
            filters={
                "keywords": keyword,
                "impact": [impact_level]
            }
        )
        count = impact_data['metadata']['totalResults']
        bar = "█" * min(count // 5, 50)
        print(f"{impact_level:8} : {count:5} {bar}")
    
    return total


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/search_keyword.py <keyword>")
        print("Example: python scripts/search_keyword.py Governor")
        sys.exit(1)
    
    keyword = " ".join(sys.argv[1:])
    
    try:
        search_by_keyword(keyword)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
