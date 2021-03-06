"""migrate three

Revision ID: 792190d1d130
Revises: 
Create Date: 2022-07-21 17:54:30.676347

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '792190d1d130'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('albums', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'albums', 'users', ['user_id'], ['user_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'albums', type_='foreignkey')
    op.drop_column('albums', 'user_id')
    # ### end Alembic commands ###
