"""Machine types: added possibility to disable authorization

Revision ID: dfd2b0db0016
Revises: aa9ed3e094d5
Create Date: 2024-05-05 20:27:50.705509

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dfd2b0db0016'
down_revision: Union[str, None] = 'aa9ed3e094d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('machine_types', sa.Column('access_management', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('machine_types', 'access_management')
    # ### end Alembic commands ###
