"""Order schemas."""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class OrderBase(BaseModel):
    """Base order schema."""

    symbol: str = Field(..., min_length=1, max_length=20)
    side: str = Field(..., pattern="^(buy|sell)$")
    quantity: float = Field(..., gt=0)
    price: float = Field(..., gt=0)
    fees: float = Field(default=0, ge=0)
    order_date: datetime
    notes: Optional[str] = None


class OrderCreate(OrderBase):
    """Schema for creating an order."""

    portfolio_id: UUID


class Order(OrderBase):
    """Schema for order response."""

    id: UUID
    portfolio_id: UUID
    total_value: Optional[float] = None
    notion_page_id: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True
