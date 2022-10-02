"""Add date

Revision ID: 2cb3479bc4a9
Revises: 30d698f26b55
Create Date: 2022-09-28 22:50:43.143636

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2cb3479bc4a9'
down_revision = '30d698f26b55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('contacts', sa.Column('birthday', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('contacts', 'birthday')
    # ### end Alembic commands ###