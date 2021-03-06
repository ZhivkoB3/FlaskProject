"""add column to payment requests - total invoice amount

Revision ID: 2ca4daa27117
Revises: b8462c00f8b0
Create Date: 2022-01-08 19:36:49.345498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ca4daa27117'
down_revision = 'b8462c00f8b0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('payment_requests', sa.Column('total_invoice_amount', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('payment_requests', 'total_invoice_amount')
    # ### end Alembic commands ###
