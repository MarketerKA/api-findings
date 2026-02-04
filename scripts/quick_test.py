#!/usr/bin/env python3
"""
Quick API test
"""
import sys
import os

# Add project root directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.solodit_client import SoloditClient


def quick_test():
    """Quick connection test"""
    print("🧪 Quick Solodit API Test")
    print("=" * 60)
    
    try:
        client = SoloditClient()
        print("✅ Client created successfully")
        
        print("\n📡 Testing connection...")
        data = client.search_findings(page=1, page_size=5)
        
        print(f"✅ Connection successful!")
        print(f"   Total findings: {data['metadata']['totalResults']}")
        print(f"   Rate limit: {data['rateLimit']['remaining']}/{data['rateLimit']['limit']}")
        
        print("\n📋 First 3 results:")
        for i, finding in enumerate(data['findings'][:3], 1):
            print(f"   {i}. [{finding['impact']}] {finding['title'][:60]}...")
        
        print("\n✅ All tests passed successfully!")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    quick_test()
