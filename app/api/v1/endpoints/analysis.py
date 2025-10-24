"""Analysis endpoints."""

from fastapi import APIRouter


router = APIRouter()


@router.post("/technical")
async def technical_analysis(symbol: str):
    """Perform technical analysis."""
    # TODO: Implement
    return {"symbol": symbol, "status": "pending"}


@router.post("/fundamental")
async def fundamental_analysis(symbol: str):
    """Perform fundamental analysis."""
    # TODO: Implement
    return {"symbol": symbol, "status": "pending"}
