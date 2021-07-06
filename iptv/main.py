from fastapi import FastAPI

from .db import database
from .shows.main import router as shows_router
from .users.main import router as users_router

app = FastAPI()
app.include_router(shows_router)
app.include_router(users_router)


@app.on_event("startup")
async def connect():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()
