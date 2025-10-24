"""Stock data endpoints."""

from fastapi import APIRouter, HTTPException, status
from app.services.market_data_service import MarketDataService


router = APIRouter()


@router.get("/{symbol}")
async def get_stock(symbol: str):
    """Get stock information."""
    service = MarketDataService()
    try:
        return await service.get_stock_info(symbol)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Stock {symbol} not found",
        )


@router.get("/{symbol}/price")
async def get_stock_price(symbol: str):
    """Get current stock price."""
    service = MarketDataService()
    return await service.get_current_price(symbol)


@router.get("/{symbol}/history")
async def get_stock_history(
    symbol: str,
    period: str = "1mo",
    interval: str = "1d",
):
    """Get historical stock data."""
    service = MarketDataService()
    return await service.get_historical_data(symbol, period, interval)
