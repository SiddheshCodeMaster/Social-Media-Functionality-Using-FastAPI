"""Add Foriegn Key to POSTS table

Revision ID: a1163e1bb0ed
Revises: 7d3f1c7ef38b
Create Date: 2023-05-07 00:11:44.318519

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1163e1bb0ed'
down_revision = '7d3f1c7ef38b'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable = False))
    op.create_foreign_key('posts_users_fk',source_table = "posts", 
                          referent_table = "users", 
                          local_cols=['owner_id'], 
                          remote_cols=['id'],
                          ondelete="cASCADE")
    pass
 

def downgrade():
    op.drop_constraint('post_users_fk',table_name="posts")
    op.drop_column("posts","owner_id")
    pass
