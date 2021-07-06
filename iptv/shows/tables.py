import sqlalchemy as sa

from iptv.db import metadata

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
