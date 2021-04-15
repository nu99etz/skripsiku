"""empty message

Revision ID: 3e39334b43a3
Revises: 713cdde9bdf3
Create Date: 2021-03-31 13:21:42.714990

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e39334b43a3'
down_revision = '713cdde9bdf3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alamat_pengiriman',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_pengiriman', sa.String(length=30), nullable=True),
    sa.Column('alamat_pengiriman', sa.Text(), nullable=False),
    sa.Column('coordinates', sa.Text(), nullable=False),
    sa.Column('lattitude', sa.Integer(), nullable=False),
    sa.Column('longitude', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=255), nullable=False),
    sa.Column('nama_pengguna', sa.Integer(), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=True),
    sa.Column('is_aktif', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['nama_pengguna'], ['kurir.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('alamat_pengiriman')
    # ### end Alembic commands ###
