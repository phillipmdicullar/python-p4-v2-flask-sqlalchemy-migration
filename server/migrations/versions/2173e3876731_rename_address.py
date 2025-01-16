"""rename address

Revision ID: 2173e3876731
Revises: 51e602e99e45
Create Date: 2025-01-16 16:48:17.616005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2173e3876731'
down_revision = '51e602e99e45'
branch_labels = None
depends_on = None

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'address',  new_column_name='location')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('departments', 'location',  new_column_name='address')
    # ### end Alembic commands ###
# def upgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.add_column('departments', sa.Column('location', sa.String(), nullable=False))
#     op.drop_column('departments', 'address')
#     # ### end Alembic commands ###


# def downgrade():
#     # ### commands auto generated by Alembic - please adjust! ###
#     op.add_column('departments', sa.Column('address', sa.VARCHAR(), nullable=True))
#     op.drop_column('departments', 'location')
#     # ### end Alembic commands ###
