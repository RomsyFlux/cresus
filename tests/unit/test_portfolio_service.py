"""Unit tests for portfolio service."""

import pytest
from uuid import uuid4
from app.services.portfolio_service import PortfolioService
from app.schemas.portfolio import PortfolioCreate


@pytest.mark.asyncio
async def test_create_portfolio(test_db):
    """Test portfolio creation."""
    service = PortfolioService(test_db)
    portfolio_data = PortfolioCreate(
        user_id=uuid4(),
        name="Test Portfolio",
        type="virtual",
        currency="USD",
        initial_capital=10000.0,
    )

    portfolio = await service.create_portfolio(portfolio_data)

    assert portfolio.name == "Test Portfolio"
    assert portfolio.type == "virtual"
    assert portfolio.currency == "USD"
    assert portfolio.is_active is True


@pytest.mark.asyncio
async def test_list_portfolios(test_db):
    """Test listing portfolios."""
    service = PortfolioService(test_db)
    portfolios = await service.list_portfolios()

    assert isinstance(portfolios, list)


@pytest.mark.asyncio
async def test_calculate_performance(test_db):
    """Test portfolio performance calculation."""
    service = PortfolioService(test_db)
    user_id = uuid4()

    # Create a test portfolio
    portfolio_data = PortfolioCreate(
        user_id=user_id,
        name="Performance Test",
        type="virtual",
        initial_capital=10000.0,
    )
    portfolio = await service.create_portfolio(portfolio_data)

    # Calculate performance
    performance = await service.calculate_performance(portfolio.id)

    assert "total_value" in performance
    assert "total_return_percent" in performance
    assert performance["num_positions"] == 0
