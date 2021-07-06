"""Create authtoken table

Revision ID: d6ba3929f752
Revises: faaa9118a00d
Create Date: 2021-07-07 01:57:16.653514

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d6ba3929f752"
down_revision = "faaa9118a00d"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "authtokens",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column(
            "user", sa.Integer, sa.ForeignKey("users.id", ondelete="CASCADE")
        ),
        sa.Column("token", sa.String),
    )


def downgrade():
    op.drop_table("authtokens")
