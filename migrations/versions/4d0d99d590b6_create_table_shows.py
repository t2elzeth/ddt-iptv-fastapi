"""Create table shows

Revision ID: 4d0d99d590b6
Revises: 
Create Date: 2021-07-05 19:03:50.896339

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "4d0d99d590b6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "shows",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String),
        sa.Column("rating", sa.Integer),
        sa.Column("type", sa.String),
        sa.Column("description", sa.Text),
        sa.Column("genre", sa.String),
    )


def downgrade():
    op.drop_table("shows")
