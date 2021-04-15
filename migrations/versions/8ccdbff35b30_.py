"""empty message

Revision ID: 8ccdbff35b30
Revises: 5b1fc11fb563
Create Date: 2021-03-31 14:09:46.308222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ccdbff35b30'
down_revision = '5b1fc11fb563'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alamat_pengiriman',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_pengiriman', sa.String(length=30), nullable=True),
    sa.Column('alamat_pengiriman', sa.Text(), nullable=False),
    sa.Column('coordinates', sa.Text(), nullable=False),
    sa.Column('lattitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
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
