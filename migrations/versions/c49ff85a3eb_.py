"""empty message

Revision ID: c49ff85a3eb
Revises: 31f42b7a560e
Create Date: 2015-08-30 12:25:10.316340

"""

# revision identifiers, used by Alembic.
revision = 'c49ff85a3eb'
down_revision = '31f42b7a560e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('lastseen', sa.DateTime(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'lastseen')
    ### end Alembic commands ###
