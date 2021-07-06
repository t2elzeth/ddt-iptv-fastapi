from fastapi import APIRouter, HTTPException, status

from iptv.db import database
from iptv.users import hashing, schemas
from iptv.users.tables import users

router = APIRouter()


@router.post("/", response_model=schemas.ShowSingleUser)
async def create_user(payload: schemas.CreateUser):
    query = (
        users.select()
        .where(users.c.email == payload.email)
        .with_only_columns(users.c.email)
    )

    user = await database.fetch_one(query)
    if user is not None:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="User exists"
        )

    hashed_password = hashing.bcrypt(payload.password)
    query = users.insert().values(
        email=payload.email, password=hashed_password
    )

    record_id = await database.execute(query)
    query = (
        users.select()
        .where(users.c.id == record_id)
        .with_only_columns(
            users.c.id,
            users.c.email,
            users.c.is_active,
            users.c.is_staff,
            users.c.is_superuser,
        )
    )
    user = await database.fetch_one(query)
    return user


@router.get("/{pk}", response_model=schemas.ShowSingleUser)
async def get_one(pk: int):
    query = (
        users.select()
        .where(users.c.id == pk)
        .with_only_columns(
            users.c.id,
            users.c.email,
            users.c.is_active,
            users.c.is_staff,
            users.c.is_superuser,
        )
    )
    return await database.fetch_one(query)


@router.patch("/{pk}", response_model=schemas.ShowSingleUser)
async def update_one(pk: int, payload: schemas.PatchUser):
    query = (
        users.update()
        .where(users.c.id == pk)
        .values(email=payload.email, is_active=payload.is_active)
    )
    await database.execute(query)

    query = users.select().where(users.c.id == pk)
    return await database.fetch_one(query)
