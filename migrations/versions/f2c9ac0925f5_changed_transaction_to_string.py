"""changed transaction to string

Revision ID: f2c9ac0925f5
Revises: d02a442495c3
Create Date: 2023-07-14 17:33:38.142894

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2c9ac0925f5'
down_revision = 'd02a442495c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tenant_transactions', schema=None) as batch_op:
        batch_op.alter_column('transaction',
               existing_type=sa.INTEGER(),
               type_=sa.String(),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('tenant_transactions', schema=None) as batch_op:
        batch_op.alter_column('transaction',
               existing_type=sa.String(),
               type_=sa.INTEGER(),
               existing_nullable=True)

    # ### end Alembic commands ###
