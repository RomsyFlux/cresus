"""Stock model."""

from datetime import datetime
from sqlalchemy import Column, String, DateTime, BigInteger, JSON

from app.core.database import Base


class Stock(Base):
    """Stock model."""

    __tablename__ = "stocks"

    symbol = Column(String(20), primary_key=True)
    name = Column(String(255), nullable=True)
    exchange = Column(String(50), nullable=True)
    sector = Column(String(100), nullable=True)
    industry = Column(String(100), nullable=True)
    market_cap = Column(BigInteger, nullable=True)
    metadata = Column(JSON, default={})
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
