"""empty message

Revision ID: 653f0880b1dd
Revises: bce5fd36b371
Create Date: 2021-04-26 00:56:00.080367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '653f0880b1dd'
down_revision = 'bce5fd36b371'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('requests',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created', sa.DateTime(), server_default=sa.text('now()'), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=False),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('duration', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('requests')
    # ### end Alembic commands ###