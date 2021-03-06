"""empty message

Revision ID: a5566f693c72
Revises: 8ccdbff35b30
Create Date: 2021-04-01 12:03:40.826099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a5566f693c72'
down_revision = '8ccdbff35b30'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('login',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('is_aktif', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('user')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('nama_pengguna', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('is_aktif', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['nama_pengguna'], ['kurir.id'], name='user_nama_pengguna_fkey'),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.drop_table('login')
    # ### end Alembic commands ###
