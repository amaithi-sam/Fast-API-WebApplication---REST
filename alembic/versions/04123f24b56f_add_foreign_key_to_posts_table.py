"""add foreign-key to posts table

Revision ID: 04123f24b56f
Revises: cb4f269d285a
Create Date: 2022-07-12 18:06:57.367771

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '04123f24b56f'
down_revision = 'cb4f269d285a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts',
                  sa.Column('owner_id', sa.Integer(), nullable=False)
                  )
    op.create_foreign_key('post_users_fk',
                          source_table="posts",
                          referent_table="users",
                          local_cols=['owner_id'],
                          remote_cols=['id'],
                          ondelete='CASCADE'
                          )
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column(table_name="posts", column_name="owner_id")

    pass
