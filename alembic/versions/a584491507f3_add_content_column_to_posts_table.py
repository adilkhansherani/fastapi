"""add content column to posts table

Revision ID: a584491507f3
Revises: 26d33291ec99
Create Date: 2023-07-13 17:14:37.441658

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a584491507f3'
down_revision = '26d33291ec99'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
