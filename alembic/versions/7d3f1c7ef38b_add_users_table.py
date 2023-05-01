"""Add USERS Table

Revision ID: 7d3f1c7ef38b
Revises: c819c65d115e
Create Date: 2023-05-01 14:48:59.935075

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7d3f1c7ef38b'
down_revision = 'c819c65d115e'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users', 
                    sa.Column('id',sa.Integer(), nullable = False),
                    sa.Column('email', sa.String(), nullable = False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone = True), 
                              server_default = sa.text('now()'), nullable = False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
