"""Add last few columns to posts table

Revision ID: 114223e1ea26
Revises: a1163e1bb0ed
Create Date: 2023-05-07 00:28:09.491520

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '114223e1ea26'
down_revision = 'a1163e1bb0ed'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts',sa.Column(
        'published', sa.Boolean(), nullable = False, server_default = 'TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default = sa.text
        ('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts','published')
    op.drop_column('posts','created_at')
    pass
