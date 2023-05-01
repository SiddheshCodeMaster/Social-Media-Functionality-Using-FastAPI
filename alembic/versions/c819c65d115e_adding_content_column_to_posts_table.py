"""Adding content column to POSTS table

Revision ID: c819c65d115e
Revises: 104b0c90e3ae
Create Date: 2023-05-01 14:45:22.752164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c819c65d115e'
down_revision = '104b0c90e3ae'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable = False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass
