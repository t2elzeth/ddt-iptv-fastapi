from fastapi import APIRouter

router = APIRouter(prefix="/shows", tags=["shows"])


@router.get("")
def shows_index():
    """Blog index route"""
    return "This is a shows index page"


@router.get("/last")
def shows_last():
    """Get last shows"""
    return "Shows last "


@router.get("/{id}")
def shows_retrieve(id):
    return f"Retrieving show ID:{id}"
