"""Google Sheets API client."""

from typing import List, Dict, Optional
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from app.core.config import settings
from app.core.logging import logger


class GoogleSheetsClient:
    """Client for Google Sheets API integration."""

    SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

    def __init__(self):
        try:
            credentials = service_account.Credentials.from_service_account_file(
                settings.GOOGLE_SHEETS_CREDENTIALS_PATH,
                scopes=self.SCOPES,
            )
            self.service = build("sheets", "v4", credentials=credentials)
        except Exception as e:
            logger.warning("Failed to initialize Google Sheets client", error=str(e))
            self.service = None

    async def read_range(self, spreadsheet_id: str, range_name: str) -> List[List]:
        """Read data from a spreadsheet range."""
        if not self.service:
            raise ValueError("Google Sheets client not initialized")

        try:
            result = (
                self.service.spreadsheets()
                .values()
                .get(spreadsheetId=spreadsheet_id, range=range_name)
                .execute()
            )
            return result.get("values", [])
        except HttpError as e:
            logger.error("Failed to read from Google Sheets", error=str(e))
            raise

    async def write_range(
        self, spreadsheet_id: str, range_name: str, values: List[List]
    ) -> Dict:
        """Write data to a spreadsheet range."""
        if not self.service:
            raise ValueError("Google Sheets client not initialized")

        try:
            body = {"values": values}
            result = (
                self.service.spreadsheets()
                .values()
                .update(
                    spreadsheetId=spreadsheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    body=body,
                )
                .execute()
            )
            return result
        except HttpError as e:
            logger.error("Failed to write to Google Sheets", error=str(e))
            raise

    async def append_rows(
        self, spreadsheet_id: str, range_name: str, values: List[List]
    ) -> Dict:
        """Append rows to a spreadsheet."""
        if not self.service:
            raise ValueError("Google Sheets client not initialized")

        try:
            body = {"values": values}
            result = (
                self.service.spreadsheets()
                .values()
                .append(
                    spreadsheetId=spreadsheet_id,
                    range=range_name,
                    valueInputOption="RAW",
                    insertDataOption="INSERT_ROWS",
                    body=body,
                )
                .execute()
            )
            return result
        except HttpError as e:
            logger.error("Failed to append to Google Sheets", error=str(e))
            raise

    async def sync_portfolio_data(self, spreadsheet_id: str, portfolio_data: Dict) -> Dict:
        """Sync portfolio data to Google Sheets."""
        # Prepare data rows
        headers = [
            "Date",
            "Portfolio",
            "Total Value",
            "Cash",
            "Invested",
            "Total Return",
            "Total Return %",
        ]

        data_row = [
            portfolio_data.get("date", ""),
            portfolio_data.get("name", ""),
            portfolio_data.get("total_value", 0),
            portfolio_data.get("cash", 0),
            portfolio_data.get("invested", 0),
            portfolio_data.get("total_return", 0),
            portfolio_data.get("total_return_percent", 0),
        ]

        # Append data
        return await self.append_rows(spreadsheet_id, "Portfolio Performance!A:G", [data_row])
