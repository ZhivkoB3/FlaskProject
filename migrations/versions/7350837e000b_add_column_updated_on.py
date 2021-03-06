"""add column updated_on

Revision ID: 7350837e000b
Revises: b160ef6078ee
Create Date: 2021-12-27 13:19:57.220450

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7350837e000b'
down_revision = 'b160ef6078ee'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Daily Water consumption_pk', table_name='Daily Water consumption')
    op.drop_table('Daily Water consumption')
    op.add_column('compressors', sa.Column('updated_on', sa.DateTime(), nullable=True))
    op.add_column('electricity', sa.Column('updated_on', sa.DateTime(), nullable=True))
    op.add_column('natural_gas', sa.Column('updated_on', sa.DateTime(), nullable=True))
    op.add_column('water', sa.Column('updated_on', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('water', 'updated_on')
    op.drop_column('natural_gas', 'updated_on')
    op.drop_column('electricity', 'updated_on')
    op.drop_column('compressors', 'updated_on')
    op.create_table('Daily Water consumption',
    sa.Column('pk', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_m3', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('high_pressure_casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('glazing', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('sorting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('administration', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('data_entry_id', sa.BIGINT(), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Daily Water consumption_pk', 'Daily Water consumption', ['pk'], unique=False)
    # ### end Alembic commands ###
