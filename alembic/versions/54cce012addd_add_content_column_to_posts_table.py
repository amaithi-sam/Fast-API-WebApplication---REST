"""add content column to posts table

Revision ID: 54cce012addd
Revises: 92c7d2101632
Create Date: 2022-07-12 16:17:59.596410

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54cce012addd'
down_revision = '92c7d2101632'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
