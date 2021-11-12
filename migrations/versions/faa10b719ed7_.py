"""empty message

Revision ID: faa10b719ed7
Revises: 2da743294aa0
Create Date: 2021-10-14 16:29:36.089566

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'faa10b719ed7'
down_revision = '2da743294aa0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('book', sa.Column('description', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('book', 'description')
    # ### end Alembic commands ###
