"""Add Last few columns to post table

Revision ID: 148b594b101d
Revises: 04123f24b56f
Create Date: 2022-07-12 18:20:43.224263

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '148b594b101d'
down_revision = '04123f24b56f'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column(
        table_name='posts',
        column= sa.Column('published', sa.Boolean(), nullable=False, server_default='True')
    )
    op.add_column(
        table_name="posts",
        column= sa.Column(
            'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text("NOW()")
        )
    )
    pass


def downgrade() -> None:
    op.drop_column(table_name='posts', column_name='published')
    op.drop_column(table_name='posts', column_name='created_at')
    pass
