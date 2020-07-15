"""empty message

Revision ID: 270d39d23a18
Revises: b74955ec2b8c
Create Date: 2020-07-15 13:25:30.528187

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '270d39d23a18'
down_revision = 'b74955ec2b8c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('genres', sa.String(length=500), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Artist', sa.Column('seeking_venue', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('website', sa.String(length=500), nullable=True))
    op.drop_column('Artist', 'website_link')
    op.add_column('Show', sa.Column('start_time', sa.DateTime(), nullable=True))
    op.drop_column('Show', 'datetime')
    op.add_column('Venue', sa.Column('num_upcoming_shows', sa.Integer(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=500), nullable=True))
    op.add_column('Venue', sa.Column('seeking_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('website', sa.String(length=500), nullable=True))
    op.drop_column('Venue', 'website_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Venue', sa.Column('website_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.drop_column('Venue', 'website')
    op.drop_column('Venue', 'seeking_talent')
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'num_upcoming_shows')
    op.add_column('Show', sa.Column('datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('Show', 'start_time')
    op.add_column('Artist', sa.Column('website_link', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
    op.drop_column('Artist', 'website')
    op.drop_column('Artist', 'seeking_venue')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'genres')
    # ### end Alembic commands ###
