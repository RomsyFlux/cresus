"""Order model."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Numeric, Text, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Order(Base):
    """Order model."""

    __tablename__ = "orders"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    portfolio_id = Column(UUID(as_uuid=True), ForeignKey("portfolios.id", ondelete="CASCADE"), nullable=False)
    symbol = Column(String(20), nullable=False, index=True)
    side = Column(String(10), nullable=False)  # 'buy' or 'sell'
    quantity = Column(Numeric(15, 4), nullable=False)
    price = Column(Numeric(15, 4), nullable=False)
    total_value = Column(Numeric(15, 2), nullable=True)
    fees = Column(Numeric(15, 2), default=0)
    order_date = Column(DateTime, nullable=False)
    notes = Column(Text, nullable=True)
    notion_page_id = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    portfolio = relationship("Portfolio", back_populates="orders")
