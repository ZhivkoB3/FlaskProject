"""add some changes on payment_requests table

Revision ID: 1dd9738b04a3
Revises: 2ca4daa27117
Create Date: 2022-01-08 21:56:23.033560

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '1dd9738b04a3'
down_revision = '2ca4daa27117'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Daily electricity consumption_pk', table_name='Daily electricity consumption')
    op.drop_table('Daily electricity consumption')
    op.drop_index('ix_Daily compressors consumption_pk', table_name='Daily compressors consumption')
    op.drop_table('Daily compressors consumption')
    op.drop_index('ix_Daily Water consumption_pk', table_name='Daily Water consumption')
    op.drop_table('Daily Water consumption')
    op.drop_index('ix_Daily natural gas consumption_pk', table_name='Daily natural gas consumption')
    op.drop_table('Daily natural gas consumption')
    op.add_column('payment_requests', sa.Column('updated_on', sa.DateTime(), nullable=True))
    op.add_column('payment_requests', sa.Column('updated_by', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'payment_requests', 'payment_receivers', ['updated_by'], ['pk'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'payment_requests', type_='foreignkey')
    op.drop_column('payment_requests', 'updated_by')
    op.drop_column('payment_requests', 'updated_on')
    op.create_table('Daily natural gas consumption',
    sa.Column('pk', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_Nm3', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('high_pressure_casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('glazing', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('sorting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('kilns', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('shuttle_kilns', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('administration', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('user_id', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Daily natural gas consumption_pk', 'Daily natural gas consumption', ['pk'], unique=False)
    op.create_table('Daily Water consumption',
    sa.Column('pk', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_m3', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('high_pressure_casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('glazing', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('sorting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('administration', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('user_id', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Daily Water consumption_pk', 'Daily Water consumption', ['pk'], unique=False)
    op.create_table('Daily compressors consumption',
    sa.Column('pk', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_kwh', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_one', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_two', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_three', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_four', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_five', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('user_id', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Daily compressors consumption_pk', 'Daily compressors consumption', ['pk'], unique=False)
    op.create_table('Daily electricity consumption',
    sa.Column('pk', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_kwh', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('high_pressure_casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('glazing', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('sorting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('kilns', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('shuttle_kilns', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('administration', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.BIGINT(), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Daily electricity consumption_pk', 'Daily electricity consumption', ['pk'], unique=False)
    # ### end Alembic commands ###
