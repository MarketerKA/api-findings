"""
Solodit API Client
Client for working with Cyfrin Solodit Findings API
"""
import os
import requests
from typing import Optional, Dict, List, Any
from dotenv import load_dotenv

# Load environment variables
load_dotenv()


class SoloditClient:
    """Client for working with Solodit API"""
    
    BASE_URL = "https://solodit.cyfrin.io/api/v1/solodit"
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize client
        
        Args:
            api_key: API key (if not specified, taken from .env)
        """
        self.api_key = api_key or os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Specify it in .env or pass to constructor")
        
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "X-Cyfrin-API-Key": self.api_key
        })
    
    def search_findings(
        self,
        page: int = 1,
        page_size: int = 50,
        filters: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """
        Search findings with filters
        
        Args:
            page: Page number (starting from 1)
            page_size: Results per page (max 100)
            filters: Dictionary with filters
        
        Returns:
            Dictionary with search results
        """
        url = f"{self.BASE_URL}/findings"
        payload = {
            "page": page,
            "pageSize": min(page_size, 100),
        }
        
        if filters:
            payload["filters"] = filters
        
        response = self.session.post(url, json=payload)
        response.raise_for_status()
        
        data = response.json()
        
        # Print rate limit information
        rate_limit = data.get("rateLimit", {})
        print(f"Rate limit: {rate_limit.get('remaining', '?')}/{rate_limit.get('limit', '?')}")
        
        return data
    
    def get_high_severity_findings(
        self,
        page: int = 1,
        page_size: int = 50,
        keywords: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get high severity findings
        
        Args:
            page: Page number
            page_size: Number of results
            keywords: Keywords to search
        
        Returns:
            Dictionary with results
        """
        filters = {"impact": ["HIGH"]}
        if keywords:
            filters["keywords"] = keywords
        
        return self.search_findings(page, page_size, filters)
    
    def search_by_firm(
        self,
        firms: List[str],
        page: int = 1,
        page_size: int = 50
    ) -> Dict[str, Any]:
        """
        Search findings by audit firms
        
        Args:
            firms: List of firm names
            page: Page number
            page_size: Number of results
        
        Returns:
            Dictionary with results
        """
        filters = {
            "firms": [{"value": firm} for firm in firms]
        }
        return self.search_findings(page, page_size, filters)
    
    def search_by_tags(
        self,
        tags: List[str],
        impact: Optional[List[str]] = None,
        page: int = 1,
        page_size: int = 50
    ) -> Dict[str, Any]:
        """
        Search findings by tags
        
        Args:
            tags: List of tags (e.g., ["Reentrancy", "Oracle"])
            impact: List of severity levels (e.g., ["HIGH", "MEDIUM"])
            page: Page number
            page_size: Number of results
        
        Returns:
            Dictionary with results
        """
        filters = {
            "tags": [{"value": tag} for tag in tags]
        }
        if impact:
            filters["impact"] = impact
        
        return self.search_findings(page, page_size, filters)
    
    def get_recent_findings(
        self,
        days: int = 30,
        page: int = 1,
        page_size: int = 50
    ) -> Dict[str, Any]:
        """
        Get recent findings
        
        Args:
            days: Number of days (30, 60, 90)
            page: Page number
            page_size: Number of results
        
        Returns:
            Dictionary with results
        """
        valid_days = {30: "30", 60: "60", 90: "90"}
        day_value = valid_days.get(days, "30")
        
        filters = {
            "reported": {"value": day_value},
            "sortField": "Recency",
            "sortDirection": "Desc"
        }
        return self.search_findings(page, page_size, filters)
