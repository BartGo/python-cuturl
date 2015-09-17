"""Add a column

Revision ID: 212ab906cad8
Revises: 63bb5f350f3
Create Date: 2015-09-17 20:22:53.100000

"""

# revision identifiers, used by Alembic.
revision = '212ab906cad8'
down_revision = '63bb5f350f3'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.add_column('account', sa.Column('last_transaction_date', sa.DateTime))

def downgrade():
    op.drop_column('account', 'last_transaction_date')
