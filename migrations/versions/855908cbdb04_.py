"""empty message

Revision ID: 855908cbdb04
Revises: 476e3e7266ce
Create Date: 2019-08-10 15:26:46.674019

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '855908cbdb04'
down_revision = '476e3e7266ce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('events', sa.Column('image', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('events', 'image')
    # ### end Alembic commands ###
