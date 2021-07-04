from fastapi import FastAPI

from .shows.main import router as shows_router

app = FastAPI()
app.include_router(shows_router)
