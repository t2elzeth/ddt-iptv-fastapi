from fastapi import APIRouter

from iptv.db import database

from . import schemas
from .tables import shows

router = APIRouter(prefix="/shows", tags=["shows"])


@router.get("", response_model=schemas.RetrieveSingleShow)
async def shows_index():
    """Blog index route"""
    query = shows.select().where(shows.c.id == 1)
    show = await database.fetch_one(query)
    return show


@router.get("/last")
def shows_last():
    """Get last shows"""
    return "Shows last "


@router.get("/{id}")
def shows_retrieve(id):
    return f"Retrieving show ID:{id}"
