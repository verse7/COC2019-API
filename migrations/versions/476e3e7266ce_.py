"""empty message

Revision ID: 476e3e7266ce
Revises: 69219be8b34c
Create Date: 2019-08-10 10:13:15.333195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '476e3e7266ce'
down_revision = '69219be8b34c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('groups',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('date_created', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_groups',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['groups.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'group_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_groups')
    op.drop_table('groups')
    # ### end Alembic commands ###
