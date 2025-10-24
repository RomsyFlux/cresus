"""Recommendation endpoints."""

from typing import List
from uuid import UUID
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db


router = APIRouter()


@router.get("/")
async def list_recommendations(db: Session = Depends(get_db)):
    """List all recommendations."""
    # TODO: Implement
    return []


@router.post("/generate")
async def generate_recommendations(
    portfolio_id: UUID,
    db: Session = Depends(get_db),
):
    """Generate AI recommendations for a portfolio."""
    # TODO: Implement
    return {"portfolio_id": str(portfolio_id), "status": "generating"}
