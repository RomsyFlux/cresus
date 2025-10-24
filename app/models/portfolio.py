"""Portfolio model."""

import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime, Boolean, Numeric, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.database import Base


class Portfolio(Base):
    """Portfolio model."""

    __tablename__ = "portfolios"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    user_id = Column(UUID(as_uuid=True), ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(255), nullable=False)
    type = Column(String(50), nullable=False)  # 'real' or 'virtual'
    currency = Column(String(3), default="USD")
    initial_capital = Column(Numeric(15, 2), nullable=True)
    notion_database_id = Column(String(255), nullable=True)
    gsheet_id = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    user = relationship("User", back_populates="portfolios")
    positions = relationship("Position", back_populates="portfolio", cascade="all, delete-orphan")
    orders = relationship("Order", back_populates="portfolio", cascade="all, delete-orphan")
    recommendations = relationship("Recommendation", back_populates="portfolio")
