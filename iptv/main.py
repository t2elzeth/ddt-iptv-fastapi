from fastapi import FastAPI

from .shows.main import router as shows_router
from .db import create_all, database

app = FastAPI()
app.include_router(shows_router)


@app.on_event("startup")
async def connect():
    create_all()
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
