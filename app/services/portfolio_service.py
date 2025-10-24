"""Portfolio management service."""

from typing import List, Optional
from uuid import UUID
from sqlalchemy.orm import Session
from decimal import Decimal

from app.models.portfolio import Portfolio
from app.models.position import Position
from app.schemas.portfolio import PortfolioCreate, PortfolioUpdate


class PortfolioService:
    """Service for portfolio management."""

    def __init__(self, db: Session):
        self.db = db

    async def list_portfolios(self, user_id: Optional[UUID] = None) -> List[Portfolio]:
        """List all portfolios, optionally filtered by user."""
        query = self.db.query(Portfolio)
        if user_id:
            query = query.filter(Portfolio.user_id == user_id)
        return query.all()

    async def get_portfolio(self, portfolio_id: UUID) -> Optional[Portfolio]:
        """Get portfolio by ID."""
        return self.db.query(Portfolio).filter(Portfolio.id == portfolio_id).first()

    async def create_portfolio(self, portfolio_data: PortfolioCreate) -> Portfolio:
        """Create a new portfolio."""
        portfolio = Portfolio(**portfolio_data.model_dump())
        self.db.add(portfolio)
        self.db.commit()
        self.db.refresh(portfolio)
        return portfolio

    async def update_portfolio(
        self, portfolio_id: UUID, portfolio_data: PortfolioUpdate
    ) -> Optional[Portfolio]:
        """Update portfolio."""
        portfolio = await self.get_portfolio(portfolio_id)
        if not portfolio:
            return None

        update_data = portfolio_data.model_dump(exclude_unset=True)
        for field, value in update_data.items():
            setattr(portfolio, field, value)

        self.db.commit()
        self.db.refresh(portfolio)
        return portfolio

    async def delete_portfolio(self, portfolio_id: UUID) -> bool:
        """Delete portfolio."""
        portfolio = await self.get_portfolio(portfolio_id)
        if not portfolio:
            return False

        self.db.delete(portfolio)
        self.db.commit()
        return True

    async def calculate_performance(self, portfolio_id: UUID) -> dict:
        """Calculate portfolio performance metrics."""
        portfolio = await self.get_portfolio(portfolio_id)
        if not portfolio:
            return {}

        positions = (
            self.db.query(Position)
            .filter(Position.portfolio_id == portfolio_id)
            .all()
        )

        total_value = Decimal("0")
        total_cost = Decimal("0")
        total_pnl = Decimal("0")

        for position in positions:
            if position.market_value:
                total_value += Decimal(str(position.market_value))
            if position.average_cost and position.quantity:
                total_cost += Decimal(str(position.average_cost)) * Decimal(
                    str(position.quantity)
                )
            if position.unrealized_pnl:
                total_pnl += Decimal(str(position.unrealized_pnl))

        total_return_pct = (
            (total_pnl / total_cost * 100) if total_cost > 0 else Decimal("0")
        )

        return {
            "portfolio_id": str(portfolio_id),
            "total_value": float(total_value),
            "total_cost": float(total_cost),
            "total_pnl": float(total_pnl),
            "total_return_percent": float(total_return_pct),
            "num_positions": len(positions),
        }
