from fastapi import APIRouter, HTTPException, status

from iptv.db import database
from iptv.users import hashing, schemas
from iptv.users.tables import authtokens, users
from iptv.users.utils import generate_authtoken

router = APIRouter()


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
