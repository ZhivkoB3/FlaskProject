"""Extend database

Revision ID: 3f8e1bd9d52b
Revises: f98aaa6b502a
Create Date: 2021-12-10 20:56:44.969625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3f8e1bd9d52b'
down_revision = 'f98aaa6b502a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('compressors', sa.Column('total_kwh', sa.Integer(), nullable=False))
    op.add_column('compressors', sa.Column('compressor_one', sa.Integer(), nullable=False))
    op.add_column('compressors', sa.Column('compressor_two', sa.Integer(), nullable=False))
    op.add_column('compressors', sa.Column('compressor_three', sa.Integer(), nullable=False))
    op.add_column('compressors', sa.Column('compressor_four', sa.Integer(), nullable=False))
    op.add_column('compressors', sa.Column('compressor_five', sa.Integer(), nullable=False))
    op.drop_column('compressors', 'kwh')
    op.add_column('electricity', sa.Column('total_kwh', sa.Integer(), nullable=False))
    op.add_column('electricity', sa.Column('casting', sa.Integer(), nullable=False))
    op.add_column('electricity', sa.Column('high_pressure_casting', sa.Integer(), nullable=False))
    op.add_column('electricity', sa.Column('glazing', sa.Integer(), nullable=False))
    op.add_column('electricity', sa.Column('sorting', sa.Integer(), nullable=False))
    op.add_column('electricity', sa.Column('kilns', sa.Integer(), nullable=False))
    op.add_column('electricity', sa.Column('shuttle_kilns', sa.Integer(), nullable=False))
    op.add_column('electricity', sa.Column('administration', sa.Integer(), nullable=False))
    op.drop_column('electricity', 'kwh')
    op.add_column('natural_gas', sa.Column('total_Nm3', sa.Integer(), nullable=False))
    op.add_column('natural_gas', sa.Column('casting', sa.Integer(), nullable=False))
    op.add_column('natural_gas', sa.Column('high_pressure_casting', sa.Integer(), nullable=False))
    op.add_column('natural_gas', sa.Column('glazing', sa.Integer(), nullable=False))
    op.add_column('natural_gas', sa.Column('sorting', sa.Integer(), nullable=False))
    op.add_column('natural_gas', sa.Column('kilns', sa.Integer(), nullable=False))
    op.add_column('natural_gas', sa.Column('shuttle_kilns', sa.Integer(), nullable=False))
    op.add_column('natural_gas', sa.Column('administration', sa.Integer(), nullable=False))
    op.drop_column('natural_gas', 'Nm3')
    op.add_column('water', sa.Column('total_m3', sa.Integer(), nullable=False))
    op.add_column('water', sa.Column('casting', sa.Integer(), nullable=False))
    op.add_column('water', sa.Column('high_pressure_casting', sa.Integer(), nullable=False))
    op.add_column('water', sa.Column('glazing', sa.Integer(), nullable=False))
    op.add_column('water', sa.Column('sorting', sa.Integer(), nullable=False))
    op.add_column('water', sa.Column('administration', sa.Integer(), nullable=False))
    op.drop_column('water', 'm3')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('water', sa.Column('m3', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('water', 'administration')
    op.drop_column('water', 'sorting')
    op.drop_column('water', 'glazing')
    op.drop_column('water', 'high_pressure_casting')
    op.drop_column('water', 'casting')
    op.drop_column('water', 'total_m3')
    op.add_column('natural_gas', sa.Column('Nm3', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('natural_gas', 'administration')
    op.drop_column('natural_gas', 'shuttle_kilns')
    op.drop_column('natural_gas', 'kilns')
    op.drop_column('natural_gas', 'sorting')
    op.drop_column('natural_gas', 'glazing')
    op.drop_column('natural_gas', 'high_pressure_casting')
    op.drop_column('natural_gas', 'casting')
    op.drop_column('natural_gas', 'total_Nm3')
    op.add_column('electricity', sa.Column('kwh', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('electricity', 'administration')
    op.drop_column('electricity', 'shuttle_kilns')
    op.drop_column('electricity', 'kilns')
    op.drop_column('electricity', 'sorting')
    op.drop_column('electricity', 'glazing')
    op.drop_column('electricity', 'high_pressure_casting')
    op.drop_column('electricity', 'casting')
    op.drop_column('electricity', 'total_kwh')
    op.add_column('compressors', sa.Column('kwh', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('compressors', 'compressor_five')
    op.drop_column('compressors', 'compressor_four')
    op.drop_column('compressors', 'compressor_three')
    op.drop_column('compressors', 'compressor_two')
    op.drop_column('compressors', 'compressor_one')
    op.drop_column('compressors', 'total_kwh')
    # ### end Alembic commands ###
