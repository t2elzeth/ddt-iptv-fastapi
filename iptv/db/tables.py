import sqlalchemy as sa

from .init_db import metadata

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("first_name", sa.String, nullable=True),
    sa.Column("last_name", sa.String, nullable=True),
    sa.Column("email", sa.String, unique=True),
    sa.Column("password", sa.String),
    sa.Column("is_active", sa.Boolean),
    sa.Column("is_staff", sa.Boolean),
    sa.Column("is_superuser", sa.Boolean),
    sa.Column("last_active", sa.DateTime),
)

shows = sa.Table(
    "shows",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String),
    sa.Column("rating", sa.Integer),
    sa.Column("type", sa.String),
    sa.Column("description", sa.Text),
    sa.Column("genre", sa.String),
)
