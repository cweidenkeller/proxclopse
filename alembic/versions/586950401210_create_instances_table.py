"""Base db schema

Revision ID: 586950401210
Revises: None
Create Date: 2014-08-28 16:16:15.059512

"""

# revision identifiers, used by Alembic.
revision = '586950401210'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table('instances',
                    sa.Column('id', sa.String(36), primary_key=True))



def downgrade():
    op.drop_table('instances')
