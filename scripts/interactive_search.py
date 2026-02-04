#!/usr/bin/env python3
"""
Interactive findings search
"""
import sys
import os

# Add project root directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def interactive_search():
    """Interactive search mode"""
    client = SoloditClient()
    
    print("=" * 60)
    print("🔍 Interactive Solodit Findings Search")
    print("=" * 60)
    print("Enter 'exit' or 'quit' to exit\n")
    
    while True:
        try:
            keyword = input("🔎 Enter keyword to search: ").strip()
            
            if keyword.lower() in ['exit', 'quit', 'q']:
                print("👋 Goodbye!")
                break
            
            if not keyword:
                print("⚠️  Please enter a keyword\n")
                continue
            
            print(f"\n🔍 Searching: '{keyword}'...")
            print("-" * 60)
            
            # Search
            data = client.search_findings(
                page=1,
                page_size=5,
                filters={"keywords": keyword}
            )
            
            total = data['metadata']['totalResults']
            print(f"✅ Found: {total} findings\n")
            
            if data['findings']:
                for i, finding in enumerate(data['findings'], 1):
                    print(f"{i}. [{finding['impact']}] {finding['title']}")
                    print(f"   Firm: {finding.get('firm_name', 'N/A')}")
                    print(f"   Quality: {finding['quality_score']}/5")
                    print()
            else:
                print("Nothing found\n")
            
            print("-" * 60 + "\n")
            
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}\n")


if __name__ == "__main__":
    try:
        interactive_search()
    except Exception as e:
        print(f"❌ Critical error: {e}")
        sys.exit(1)
