"""Initial migration.

Revision ID: 452ab9639032
Revises: 
Create Date: 2024-03-16 11:04:36.064920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '452ab9639032'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bookable',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('map_id', sa.Integer(), nullable=False),
    sa.Column('type', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('map_id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=100), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('role', sa.Enum('admin', 'employee', name='user_role_enum'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('bookable_id', sa.String(), nullable=True),
    sa.Column('date', sa.Date(), nullable=False),
    sa.Column('start', sa.Time(), nullable=False),
    sa.Column('end', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['bookable_id'], ['bookable.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('desk',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('number_available', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['bookable.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room',
    sa.Column('id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['id'], ['bookable.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('room')
    op.drop_table('desk')
    op.drop_table('booking')
    op.drop_table('user')
    op.drop_table('bookable')
    # ### end Alembic commands ###
