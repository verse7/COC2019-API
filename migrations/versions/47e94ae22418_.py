"""empty message

Revision ID: 47e94ae22418
Revises: 1e3e84a18f07
Create Date: 2019-08-10 07:51:50.274272

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '47e94ae22418'
down_revision = '1e3e84a18f07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('events',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=120), nullable=False),
    sa.Column('location', sa.String(length=255), nullable=False),
    sa.Column('manpower_quota', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('location'),
    sa.UniqueConstraint('title')
    )
    op.drop_table('event')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('event',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(length=120), autoincrement=False, nullable=False),
    sa.Column('location', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('manpower_quota', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('date_created', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='event_pkey'),
    sa.UniqueConstraint('location', name='event_location_key'),
    sa.UniqueConstraint('title', name='event_title_key')
    )
    op.drop_table('events')
    # ### end Alembic commands ###
