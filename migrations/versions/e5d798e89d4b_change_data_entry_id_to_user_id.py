"""change data_entry_id to user_id

Revision ID: e5d798e89d4b
Revises: 85257edcb829
Create Date: 2021-12-30 17:33:26.483193

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'e5d798e89d4b'
down_revision = '85257edcb829'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_Daily electricity consumption_pk', table_name='Daily electricity consumption')
    op.drop_table('Daily electricity consumption')
    op.drop_index('ix_Daily compressors consumption_pk', table_name='Daily compressors consumption')
    op.drop_table('Daily compressors consumption')
    op.drop_index('ix_Daily natural gas consumption_pk', table_name='Daily natural gas consumption')
    op.drop_table('Daily natural gas consumption')
    op.drop_index('ix_Daily Water consumption_pk', table_name='Daily Water consumption')
    op.drop_table('Daily Water consumption')
    op.add_column('compressors', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('compressors_data_entry_id_fkey', 'compressors', type_='foreignkey')
    op.create_foreign_key(None, 'compressors', 'users', ['user_id'], ['pk'])
    op.drop_column('compressors', 'data_entry_id')
    op.add_column('electricity', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('electricity_data_entry_id_fkey', 'electricity', type_='foreignkey')
    op.create_foreign_key(None, 'electricity', 'users', ['user_id'], ['pk'])
    op.drop_column('electricity', 'data_entry_id')
    op.add_column('natural_gas', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('natural_gas_data_entry_id_fkey', 'natural_gas', type_='foreignkey')
    op.create_foreign_key(None, 'natural_gas', 'users', ['user_id'], ['pk'])
    op.drop_column('natural_gas', 'data_entry_id')
    op.add_column('water', sa.Column('user_id', sa.Integer(), nullable=True))
    op.drop_constraint('water_data_entry_id_fkey', 'water', type_='foreignkey')
    op.create_foreign_key(None, 'water', 'users', ['user_id'], ['pk'])
    op.drop_column('water', 'data_entry_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('water', sa.Column('data_entry_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'water', type_='foreignkey')
    op.create_foreign_key('water_data_entry_id_fkey', 'water', 'users', ['data_entry_id'], ['pk'])
    op.drop_column('water', 'user_id')
    op.add_column('natural_gas', sa.Column('data_entry_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'natural_gas', type_='foreignkey')
    op.create_foreign_key('natural_gas_data_entry_id_fkey', 'natural_gas', 'users', ['data_entry_id'], ['pk'])
    op.drop_column('natural_gas', 'user_id')
    op.add_column('electricity', sa.Column('data_entry_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'electricity', type_='foreignkey')
    op.create_foreign_key('electricity_data_entry_id_fkey', 'electricity', 'users', ['data_entry_id'], ['pk'])
    op.drop_column('electricity', 'user_id')
    op.add_column('compressors', sa.Column('data_entry_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'compressors', type_='foreignkey')
    op.create_foreign_key('compressors_data_entry_id_fkey', 'compressors', 'users', ['data_entry_id'], ['pk'])
    op.drop_column('compressors', 'user_id')
    op.create_table('Daily Water consumption',
    sa.Column('pk', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_m3', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('high_pressure_casting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('glazing', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('sorting', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('administration', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('data_entry_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Daily Water consumption_pk', 'Daily Water consumption', ['pk'], unique=False)
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
    sa.Column('data_entry_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.TEXT(), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Daily natural gas consumption_pk', 'Daily natural gas consumption', ['pk'], unique=False)
    op.create_table('Daily compressors consumption',
    sa.Column('pk', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('created_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('total_kwh', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_one', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_two', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_three', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_four', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('compressor_five', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('data_entry_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.TEXT(), autoincrement=False, nullable=True)
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
    sa.Column('data_entry_id', sa.BIGINT(), autoincrement=False, nullable=True),
    sa.Column('updated_on', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.Column('updated_by', sa.BIGINT(), autoincrement=False, nullable=True)
    )
    op.create_index('ix_Daily electricity consumption_pk', 'Daily electricity consumption', ['pk'], unique=False)
    # ### end Alembic commands ###