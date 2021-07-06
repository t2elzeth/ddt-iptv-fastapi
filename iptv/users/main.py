import pdb

from fastapi import APIRouter, HTTPException, status

from iptv.db import database

from . import hashing, schemas
from .tables import authtokens, users
from .utils import generate_authtoken

router = APIRouter(prefix="/users")


@router.post("", response_model=schemas.ShowSingleUser)
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


@router.post("/login", response_model=schemas.ShowAuthToken)
async def create_authtoken(payload: schemas.CreateAuthToken):
    # Get user with given email address
    query = users.select().where(users.c.email == payload.email)
    user = await database.fetch_one(query)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User with the given email address not found",
        )

    # Check if token already exists
    query = authtokens.select().where(authtokens.c.user == user.get("id"))
    authtoken = await database.fetch_one(query)
    if authtoken is not None:
        return authtoken

    # Verify user's password
    password_verified = hashing.verify(user.get("password"), payload.password)
    if not password_verified:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect password",
        )

    # Create new authtoken instance in db
    query = (
        authtokens.insert()
        .values(user=user.get("id"), token=generate_authtoken())
        .returning(authtokens.c.user, authtokens.c.token)
    )
    record_id = await database.execute(query)

    # Get authtoken instance to return it back
    query = authtokens.select().where(authtokens.c.id == record_id)
    authtoken = await database.fetch_one(query)
    return authtoken
