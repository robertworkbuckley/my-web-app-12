"""empty message

Revision ID: a72bf1439a16
Revises: 3b40604fa029
Create Date: 2020-03-23 16:51:35.940404

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a72bf1439a16'
down_revision = '3b40604fa029'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('twitter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('tweet', sa.String(length=128), nullable=True),
    sa.Column('user', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('twitter')
    # ### end Alembic commands ###
