"""Create users table

Revision ID: faaa9118a00d
Revises: 4d0d99d590b6
Create Date: 2021-07-05 19:10:29.316813

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "faaa9118a00d"
down_revision = "4d0d99d590b6"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("email", sa.String, unique=True),
        sa.Column("password", sa.String),
        sa.Column("is_active", sa.Boolean, server_default="true"),
        sa.Column("is_staff", sa.Boolean, server_default="false"),
        sa.Column("is_superuser", sa.Boolean, server_default="false"),
    )


def downgrade():
    op.drop_table("users")
