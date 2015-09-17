"""create account table

Revision ID: 63bb5f350f3
Revises: 
Create Date: 2015-09-17 20:14:10.794000

"""

# revision identifiers, used by Alembic.
revision = '63bb5f350f3'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('description', sa.Unicode(200)),
    )

def downgrade():
    op.drop_table('account')
