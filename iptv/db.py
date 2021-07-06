import databases
import sqlalchemy as sa
from sqlalchemy.ext.asyncio import create_async_engine

DATABASE_URL = "postgresql://t2elzeth:postgres@localhost/db"
DATABASE_URL_SQLALCHEMY = "postgresql+asyncpg://t2elzeth:postgres@localhost/db"

metadata = sa.MetaData()

database = databases.Database(DATABASE_URL)

engine = create_async_engine(DATABASE_URL_SQLALCHEMY)
