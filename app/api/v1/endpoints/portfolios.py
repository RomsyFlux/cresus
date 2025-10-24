"""Portfolio management endpoints."""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.portfolio import Portfolio, PortfolioCreate, PortfolioUpdate
from app.services.portfolio_service import PortfolioService


router = APIRouter()


@router.get("/", response_model=List[Portfolio])
async def list_portfolios(db: Session = Depends(get_db)):
    """List all portfolios."""
    service = PortfolioService(db)
    return await service.list_portfolios()


@router.post("/", response_model=Portfolio, status_code=status.HTTP_201_CREATED)
async def create_portfolio(
    portfolio: PortfolioCreate,
    db: Session = Depends(get_db),
):
    """Create a new portfolio."""
    service = PortfolioService(db)
    return await service.create_portfolio(portfolio)


@router.get("/{portfolio_id}", response_model=Portfolio)
async def get_portfolio(
    portfolio_id: UUID,
    db: Session = Depends(get_db),
):
    """Get portfolio by ID."""
    service = PortfolioService(db)
    portfolio = await service.get_portfolio(portfolio_id)
    if not portfolio:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found",
        )
    return portfolio


@router.patch("/{portfolio_id}", response_model=Portfolio)
async def update_portfolio(
    portfolio_id: UUID,
    portfolio: PortfolioUpdate,
    db: Session = Depends(get_db),
):
    """Update portfolio."""
    service = PortfolioService(db)
    updated = await service.update_portfolio(portfolio_id, portfolio)
    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found",
        )
    return updated


@router.delete("/{portfolio_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_portfolio(
    portfolio_id: UUID,
    db: Session = Depends(get_db),
):
    """Delete portfolio."""
    service = PortfolioService(db)
    deleted = await service.delete_portfolio(portfolio_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Portfolio not found",
        )
    return None


@router.get("/{portfolio_id}/performance")
async def get_portfolio_performance(
    portfolio_id: UUID,
    db: Session = Depends(get_db),
):
    """Get portfolio performance metrics."""
    service = PortfolioService(db)
    return await service.calculate_performance(portfolio_id)
