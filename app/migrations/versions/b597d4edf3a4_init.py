"""Init

Revision ID: b597d4edf3a4
Revises: 
Create Date: 2022-04-15 14:15:20.744457

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b597d4edf3a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('genre', sa.String(), nullable=False),
    sa.Column('author', sa.String(), nullable=False),
    sa.Column('deadline', sa.Integer(), nullable=True),
    sa.Column('readed', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('book')
    # ### end Alembic commands ###