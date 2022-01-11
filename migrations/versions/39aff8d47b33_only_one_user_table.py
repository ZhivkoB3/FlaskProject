"""only one user table

Revision ID: 39aff8d47b33
Revises: 8987e3c2154c
Create Date: 2021-12-30 15:20:49.651396

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '39aff8d47b33'
down_revision = '8987e3c2154c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('pk', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(), nullable=False),
    sa.Column('last_name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('role', sa.Enum('unknown', 'bulgargaz', 'energo_pro', 'data_entry', 'data_analyst', 'accountant', 'ceo', 'user', name='roletype'), nullable=False),
    sa.PrimaryKeyConstraint('pk'),
    sa.UniqueConstraint('email')
    )
    op.drop_table('accountants')
    op.drop_index('ix_Daily compressors consumption_pk', table_name='Daily compressors consumption')
    op.drop_table('Daily compressors consumption')
    op.drop_table('data_entries')
    op.drop_index('ix_Daily Water consumption_pk', table_name='Daily Water consumption')
    op.drop_table('Daily Water consumption')
    op.drop_index('ix_Daily electricity consumption_pk', table_name='Daily electricity consumption')
    op.drop_table('Daily electricity consumption')
    op.drop_table('data_analysts')
    op.drop_table('CEO')
    op.drop_index('ix_Daily natural gas consumption_pk', table_name='Daily natural gas consumption')
    op.drop_table('Daily natural gas consumption')
    op.drop_constraint('compressors_updated_by_fkey', 'compressors', type_='foreignkey')
    op.drop_constraint('compressors_data_entry_id_fkey', 'compressors', type_='foreignkey')
    op.create_foreign_key(None, 'compressors', 'users', ['data_entry_id'], ['pk'])
    op.create_foreign_key(None, 'compressors', 'users', ['updated_by'], ['pk'])
    op.drop_constraint('electricity_data_entry_id_fkey', 'electricity', type_='foreignkey')
    op.drop_constraint('electricity_updated_by_fkey', 'electricity', type_='foreignkey')
    op.create_foreign_key(None, 'electricity', 'users', ['data_entry_id'], ['pk'])
    op.create_foreign_key(None, 'electricity', 'users', ['updated_by'], ['pk'])
    op.drop_constraint('natural_gas_updated_by_fkey', 'natural_gas', type_='foreignkey')
    op.drop_constraint('natural_gas_data_entry_id_fkey', 'natural_gas', type_='foreignkey')
    op.create_foreign_key(None, 'natural_gas', 'users', ['updated_by'], ['pk'])
    op.create_foreign_key(None, 'natural_gas', 'users', ['data_entry_id'], ['pk'])
    op.drop_constraint('water_updated_by_fkey', 'water', type_='foreignkey')
    op.drop_constraint('water_data_entry_id_fkey', 'water', type_='foreignkey')
    op.create_foreign_key(None, 'water', 'users', ['updated_by'], ['pk'])
    op.create_foreign_key(None, 'water', 'users', ['data_entry_id'], ['pk'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'water', type_='foreignkey')
    op.drop_constraint(None, 'water', type_='foreignkey')
    op.create_foreign_key('water_data_entry_id_fkey', 'water', 'data_entries', ['data_entry_id'], ['pk'])
    op.create_foreign_key('water_updated_by_fkey', 'water', 'data_entries', ['updated_by'], ['pk'])
    op.drop_constraint(None, 'natural_gas', type_='foreignkey')
    op.drop_constraint(None, 'natural_gas', type_='foreignkey')
    op.create_foreign_key('natural_gas_data_entry_id_fkey', 'natural_gas', 'data_entries', ['data_entry_id'], ['pk'])
    op.create_foreign_key('natural_gas_updated_by_fkey', 'natural_gas', 'data_entries', ['updated_by'], ['pk'])
    op.drop_constraint(None, 'electricity', type_='foreignkey')
    op.drop_constraint(None, 'electricity', type_='foreignkey')
    op.create_foreign_key('electricity_updated_by_fkey', 'electricity', 'data_entries', ['updated_by'], ['pk'])
    op.create_foreign_key('electricity_data_entry_id_fkey', 'electricity', 'data_entries', ['data_entry_id'], ['pk'])
    op.drop_constraint(None, 'compressors', type_='foreignkey')
    op.drop_constraint(None, 'compressors', type_='foreignkey')
    op.create_foreign_key('compressors_data_entry_id_fkey', 'compressors', 'data_entries', ['data_entry_id'], ['pk'])
    op.create_foreign_key('compressors_updated_by_fkey', 'compressors', 'data_entries', ['updated_by'], ['pk'])
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
    op.create_table('CEO',
    sa.Column('pk', sa.INTEGER(), server_default=sa.text('nextval(\'"CEO_pk_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('role', postgresql.ENUM('unknown', 'bulgargaz', 'energo_pro', 'data_entry', 'data_analyst', 'accountant', 'ceo', name='roletype'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('pk', name='CEO_pkey'),
    sa.UniqueConstraint('email', name='CEO_email_key')
    )
    op.create_table('data_analysts',
    sa.Column('pk', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('role', postgresql.ENUM('unknown', 'bulgargaz', 'energo_pro', 'data_entry', 'data_analyst', 'accountant', 'ceo', name='roletype'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('pk', name='data_analysts_pkey'),
    sa.UniqueConstraint('email', name='data_analysts_email_key')
    )
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
    op.create_table('data_entries',
    sa.Column('pk', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('role', postgresql.ENUM('unknown', 'bulgargaz', 'energo_pro', 'data_entry', 'data_analyst', 'accountant', 'ceo', name='roletype'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('pk', name='data_entries_pkey'),
    sa.UniqueConstraint('email', name='data_entries_email_key')
    )
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
    op.create_table('accountants',
    sa.Column('pk', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('role', postgresql.ENUM('unknown', 'bulgargaz', 'energo_pro', 'data_entry', 'data_analyst', 'accountant', 'ceo', name='roletype'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('pk', name='accountants_pkey'),
    sa.UniqueConstraint('email', name='accountants_email_key')
    )
    op.drop_table('users')
    # ### end Alembic commands ###
