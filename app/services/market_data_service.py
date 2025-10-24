"""Market data fetching service."""

import yfinance as yf
from typing import Dict, List, Optional
from datetime import datetime
import pandas as pd

from app.core.logging import logger


class MarketDataService:
    """Service for fetching market data."""

    def __init__(self):
        self.cache = {}  # Simple in-memory cache

    async def get_stock_info(self, symbol: str) -> Dict:
        """Get comprehensive stock information."""
        try:
            ticker = yf.Ticker(symbol)
            info = ticker.info

            return {
                "symbol": symbol.upper(),
                "name": info.get("longName", ""),
                "sector": info.get("sector", ""),
                "industry": info.get("industry", ""),
                "market_cap": info.get("marketCap"),
                "current_price": info.get("currentPrice"),
                "previous_close": info.get("previousClose"),
                "open": info.get("open"),
                "day_high": info.get("dayHigh"),
                "day_low": info.get("dayLow"),
                "volume": info.get("volume"),
                "pe_ratio": info.get("trailingPE"),
                "forward_pe": info.get("forwardPE"),
                "dividend_yield": info.get("dividendYield"),
                "fifty_two_week_high": info.get("fiftyTwoWeekHigh"),
                "fifty_two_week_low": info.get("fiftyTwoWeekLow"),
            }
        except Exception as e:
            logger.error("Failed to fetch stock info", symbol=symbol, error=str(e))
            raise

    async def get_current_price(self, symbol: str) -> Dict:
        """Get current stock price."""
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period="1d")

            if data.empty:
                raise ValueError(f"No data found for {symbol}")

            latest = data.iloc[-1]
            return {
                "symbol": symbol.upper(),
                "price": float(latest["Close"]),
                "timestamp": latest.name.isoformat(),
                "open": float(latest["Open"]),
                "high": float(latest["High"]),
                "low": float(latest["Low"]),
                "volume": int(latest["Volume"]),
            }
        except Exception as e:
            logger.error("Failed to fetch current price", symbol=symbol, error=str(e))
            raise

    async def get_historical_data(
        self, symbol: str, period: str = "1mo", interval: str = "1d"
    ) -> Dict:
        """Get historical stock data."""
        try:
            ticker = yf.Ticker(symbol)
            data = ticker.history(period=period, interval=interval)

            if data.empty:
                raise ValueError(f"No historical data found for {symbol}")

            history = []
            for date, row in data.iterrows():
                history.append(
                    {
                        "date": date.isoformat(),
                        "open": float(row["Open"]),
                        "high": float(row["High"]),
                        "low": float(row["Low"]),
                        "close": float(row["Close"]),
                        "volume": int(row["Volume"]),
                    }
                )

            return {
                "symbol": symbol.upper(),
                "period": period,
                "interval": interval,
                "data": history,
                "total_records": len(history),
            }
        except Exception as e:
            logger.error(
                "Failed to fetch historical data", symbol=symbol, error=str(e)
            )
            raise

    async def get_multiple_quotes(self, symbols: List[str]) -> Dict[str, Dict]:
        """Get quotes for multiple symbols."""
        quotes = {}
        for symbol in symbols:
            try:
                quotes[symbol] = await self.get_current_price(symbol)
            except Exception as e:
                logger.warning(f"Failed to get quote for {symbol}", error=str(e))
                quotes[symbol] = {"error": str(e)}
        return quotes
