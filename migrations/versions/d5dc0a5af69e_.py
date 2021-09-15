"""empty message

Revision ID: d5dc0a5af69e
Revises: 
Create Date: 2021-09-15 00:25:40.933245

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5dc0a5af69e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administrator',
    sa.Column('id_admin', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id_admin'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('full_name'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('apartment',
    sa.Column('id_apartment', sa.Integer(), nullable=False),
    sa.Column('num_apartment', sa.Integer(), nullable=False),
    sa.Column('floor_apartment', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_apartment'),
    sa.UniqueConstraint('num_apartment')
    )
    op.create_table('commonspace',
    sa.Column('id_commonspace', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('aforo', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id_commonspace')
    )
    op.create_table('building',
    sa.Column('id_building', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('adress', sa.String(length=80), nullable=False),
    sa.Column('region', sa.String(length=50), nullable=False),
    sa.Column('comuna', sa.String(length=50), nullable=False),
    sa.Column('administrator_id', sa.Integer(), nullable=True),
    sa.Column('commonspace_id', sa.Integer(), nullable=True),
    sa.Column('apartment_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['administrator_id'], ['administrator.id_admin'], ),
    sa.ForeignKeyConstraint(['apartment_id'], ['apartment.id_apartment'], ),
    sa.ForeignKeyConstraint(['commonspace_id'], ['commonspace.id_commonspace'], ),
    sa.PrimaryKeyConstraint('id_building')
    )
    op.create_table('diariomural',
    sa.Column('id_diariomural', sa.Integer(), nullable=False),
    sa.Column('administrator_id', sa.Integer(), nullable=True),
    sa.Column('announcement', sa.String(length=200), nullable=False),
    sa.ForeignKeyConstraint(['administrator_id'], ['administrator.id_admin'], ),
    sa.PrimaryKeyConstraint('id_diariomural')
    )
    op.create_table('user',
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(length=16), nullable=False),
    sa.Column('id_apartment', sa.Integer(), nullable=True),
    sa.Column('id_store', sa.Integer(), nullable=True),
    sa.Column('id_building', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_apartment'], ['apartment.id_apartment'], ),
    sa.ForeignKeyConstraint(['id_building'], ['building.id_building'], ),
    sa.PrimaryKeyConstraint('id_user'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('full_name'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('marketplace',
    sa.Column('id_marketplace', sa.Integer(), nullable=False),
    sa.Column('announcement', sa.String(length=200), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id_user'], ),
    sa.PrimaryKeyConstraint('id_marketplace')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('marketplace')
    op.drop_table('user')
    op.drop_table('diariomural')
    op.drop_table('building')
    op.drop_table('commonspace')
    op.drop_table('apartment')
    op.drop_table('administrator')
    # ### end Alembic commands ###
