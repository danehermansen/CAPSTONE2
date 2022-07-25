"""please

Revision ID: 61344e3d05b2
Revises: 85db065787ab
Create Date: 2022-07-23 20:42:49.949633

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '61344e3d05b2'
down_revision = '85db065787ab'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('albums')
    op.drop_table('reactions')
    op.drop_table('users')
    op.drop_table('comments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('comment_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('album_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('comment', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['album_id'], ['albums.album_id'], name='comments_album_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='comments_user_id_fkey'),
    sa.PrimaryKeyConstraint('comment_id', name='comments_pkey')
    )
    op.create_table('users',
    sa.Column('user_id', sa.INTEGER(), server_default=sa.text("nextval('users_user_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('username', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('password', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('user_id', name='users_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('reactions',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('album_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('likes', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['album_id'], ['albums.album_id'], name='reactions_album_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='reactions_user_id_fkey'),
    sa.PrimaryKeyConstraint('likes', name='reactions_pkey')
    )
    op.create_table('albums',
    sa.Column('album_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('album_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], name='albums_user_id_fkey'),
    sa.PrimaryKeyConstraint('album_id', name='albums_pkey')
    )
    # ### end Alembic commands ###