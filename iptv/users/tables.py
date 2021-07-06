import sqlalchemy as sa

from iptv.db import metadata

users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("email", sa.String, unique=True),
    sa.Column("password", sa.String),
    sa.Column("is_active", sa.Boolean),
    sa.Column("is_staff", sa.Boolean),
    sa.Column("is_superuser", sa.Boolean),
)
