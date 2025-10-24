"""Portfolio schemas."""

from datetime import datetime
from typing import Optional
from uuid import UUID
from pydantic import BaseModel, Field


class PortfolioBase(BaseModel):
    """Base portfolio schema."""

    name: str = Field(..., min_length=1, max_length=255)
    type: str = Field(..., pattern="^(real|virtual)$")
    currency: str = Field(default="USD", min_length=3, max_length=3)
    initial_capital: Optional[float] = None
    notion_database_id: Optional[str] = None
    gsheet_id: Optional[str] = None


class PortfolioCreate(PortfolioBase):
    """Schema for creating a portfolio."""

    user_id: UUID


class PortfolioUpdate(BaseModel):
    """Schema for updating a portfolio."""

    name: Optional[str] = Field(None, min_length=1, max_length=255)
    is_active: Optional[bool] = None
    notion_database_id: Optional[str] = None
    gsheet_id: Optional[str] = None


class Portfolio(PortfolioBase):
    """Schema for portfolio response."""

    id: UUID
    user_id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
