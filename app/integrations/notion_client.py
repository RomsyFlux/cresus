"""Notion API client."""

from typing import Dict, List, Optional
from notion_client import Client
from app.core.config import settings
from app.core.logging import logger


class NotionClient:
    """Client for Notion API integration."""

    def __init__(self):
        if not settings.NOTION_API_KEY:
            logger.warning("Notion API key not configured")
            self.client = None
        else:
            self.client = Client(auth=settings.NOTION_API_KEY)

    async def query_database(self, database_id: str, filter_params: Optional[Dict] = None) -> List[Dict]:
        """Query a Notion database."""
        if not self.client:
            raise ValueError("Notion client not initialized")

        try:
            response = self.client.databases.query(
                database_id=database_id,
                filter=filter_params or {},
            )
            return response.get("results", [])
        except Exception as e:
            logger.error("Failed to query Notion database", database_id=database_id, error=str(e))
            raise

    async def create_page(self, parent_id: str, properties: Dict, children: Optional[List] = None) -> Dict:
        """Create a new page in Notion."""
        if not self.client:
            raise ValueError("Notion client not initialized")

        try:
            page_data = {
                "parent": {"database_id": parent_id},
                "properties": properties,
            }
            if children:
                page_data["children"] = children

            response = self.client.pages.create(**page_data)
            return response
        except Exception as e:
            logger.error("Failed to create Notion page", parent_id=parent_id, error=str(e))
            raise

    async def update_page(self, page_id: str, properties: Dict) -> Dict:
        """Update a Notion page."""
        if not self.client:
            raise ValueError("Notion client not initialized")

        try:
            response = self.client.pages.update(
                page_id=page_id,
                properties=properties,
            )
            return response
        except Exception as e:
            logger.error("Failed to update Notion page", page_id=page_id, error=str(e))
            raise

    async def get_page(self, page_id: str) -> Dict:
        """Get a Notion page."""
        if not self.client:
            raise ValueError("Notion client not initialized")

        try:
            response = self.client.pages.retrieve(page_id=page_id)
            return response
        except Exception as e:
            logger.error("Failed to get Notion page", page_id=page_id, error=str(e))
            raise

    async def sync_portfolio_to_notion(self, portfolio: Dict, database_id: str) -> Dict:
        """Sync portfolio data to Notion database."""
        properties = {
            "Name": {"title": [{"text": {"content": portfolio["name"]}}]},
            "Type": {"select": {"name": portfolio["type"].capitalize()}},
            "Current Value": {"number": portfolio.get("total_value", 0)},
            "Total Return %": {"number": portfolio.get("total_return_percent", 0)},
            "Status": {"select": {"name": "Active" if portfolio.get("is_active") else "Archived"}},
        }

        # Check if page already exists
        if portfolio.get("notion_database_id"):
            return await self.update_page(portfolio["notion_database_id"], properties)
        else:
            return await self.create_page(database_id, properties)
