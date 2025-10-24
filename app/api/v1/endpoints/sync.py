"""Sync endpoints."""

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db


router = APIRouter()


@router.post("/notion")
async def sync_notion(db: Session = Depends(get_db)):
    """Trigger Notion sync."""
    # TODO: Implement
    return {"status": "syncing", "target": "notion"}


@router.post("/gsheet")
async def sync_gsheet(db: Session = Depends(get_db)):
    """Trigger Google Sheets sync."""
    # TODO: Implement
    return {"status": "syncing", "target": "gsheet"}


@router.get("/status")
async def sync_status(db: Session = Depends(get_db)):
    """Get sync status."""
    # TODO: Implement
    return {"status": "idle", "last_sync": None}
