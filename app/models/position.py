"""Position model."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Position(Base):
    """Position model."""

    __tablename__ = "positions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    portfolio_id = Column(UUID(as_uuid=True), ForeignKey("portfolios.id", ondelete="CASCADE"), nullable=False)
    symbol = Column(String(20), nullable=False, index=True)
    quantity = Column(Numeric(15, 4), nullable=False)
    average_cost = Column(Numeric(15, 4), nullable=True)
    current_price = Column(Numeric(15, 4), nullable=True)
    market_value = Column(Numeric(15, 2), nullable=True)
    unrealized_pnl = Column(Numeric(15, 2), nullable=True)
    unrealized_pnl_percent = Column(Numeric(10, 4), nullable=True)
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    portfolio = relationship("Portfolio", back_populates="positions")
