"""Recommendation model."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Numeric, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Recommendation(Base):
    """Recommendation model."""

    __tablename__ = "recommendations"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    portfolio_id = Column(UUID(as_uuid=True), ForeignKey("portfolios.id"), nullable=True)
    symbol = Column(String(20), nullable=False, index=True)
    action = Column(String(20), nullable=False)  # 'buy', 'sell', 'hold'
    confidence_score = Column(Numeric(5, 4), nullable=True)  # 0-1
    reasoning = Column(Text, nullable=False)
    target_price = Column(Numeric(15, 4), nullable=True)
    stop_loss = Column(Numeric(15, 4), nullable=True)
    time_horizon = Column(String(50), nullable=True)  # 'short-term', 'medium-term', 'long-term'
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    expires_at = Column(DateTime, nullable=True)
    status = Column(String(20), default="active")  # 'active', 'executed', 'expired'

    # Relationships
    portfolio = relationship("Portfolio", back_populates="recommendations")
