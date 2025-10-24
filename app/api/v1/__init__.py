"""API v1 router."""

from fastapi import APIRouter

from app.api.v1.endpoints import (
    portfolios,
    orders,
    stocks,
    analysis,
    recommendations,
    sync,
)

api_router = APIRouter()

api_router.include_router(
    portfolios.router,
    prefix="/portfolios",
    tags=["portfolios"],
)

api_router.include_router(
    orders.router,
    prefix="/orders",
    tags=["orders"],
)

api_router.include_router(
    stocks.router,
    prefix="/stocks",
    tags=["stocks"],
)

api_router.include_router(
    analysis.router,
    prefix="/analysis",
    tags=["analysis"],
)

api_router.include_router(
    recommendations.router,
    prefix="/recommendations",
    tags=["recommendations"],
)

api_router.include_router(
    sync.router,
    prefix="/sync",
    tags=["sync"],
)
