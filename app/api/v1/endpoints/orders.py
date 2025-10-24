"""Order management endpoints."""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.schemas.order import Order, OrderCreate


router = APIRouter()


@router.get("/", response_model=List[Order])
async def list_orders(db: Session = Depends(get_db)):
    """List all orders."""
    # TODO: Implement
    return []


@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
async def create_order(
    order: OrderCreate,
    db: Session = Depends(get_db),
):
    """Record a new order."""
    # TODO: Implement
    pass


@router.get("/{order_id}", response_model=Order)
async def get_order(
    order_id: UUID,
    db: Session = Depends(get_db),
):
    """Get order by ID."""
    # TODO: Implement
    pass
