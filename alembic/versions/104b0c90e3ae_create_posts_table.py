"""Create POSTS table

Revision ID: 104b0c90e3ae
Revises: 
Create Date: 2023-05-01 14:25:33.043043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '104b0c90e3ae'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable = False, primary_key = True),
                    sa.Column('title', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
