"""empty message

Revision ID: c5a275063aac
Revises: d2751f55a1d5
Create Date: 2022-08-08 19:19:59.429877

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c5a275063aac'
down_revision = 'd2751f55a1d5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('codeSnippets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('title', sa.String(length=64), nullable=True),
    sa.Column('author', sa.String(length=64), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('body', sa.Text(), nullable=True),
    sa.Column('link', sa.String(length=64), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('language', sa.String(length=64), nullable=True),
    sa.Column('tags', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.add_column('articles', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.add_column('articles', sa.Column('tags', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('articles', 'tags')
    op.drop_column('articles', 'timestamp')
    op.drop_table('codeSnippets')
    # ### end Alembic commands ###