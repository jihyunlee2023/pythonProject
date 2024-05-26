"""Add attendance column to politicians

Revision ID: 2f2bf01c8361
Revises: 804140ec9ea7
Create Date: 2024-05-24 16:56:46.692635

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2f2bf01c8361'
down_revision: Union[str, None] = '804140ec9ea7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('politicians', sa.Column('attendance', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('politicians', 'attendance')
    # ### end Alembic commands ###
