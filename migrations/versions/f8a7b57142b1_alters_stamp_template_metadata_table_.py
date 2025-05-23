"""alters stamp_template_metadata table; adds 'position' column

Revision ID: f8a7b57142b1
Revises: cb1b1f3db18a
Create Date: 2025-04-10 13:51:46.276158

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = 'f8a7b57142b1'
down_revision = 'cb1b1f3db18a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stamp_template_metadata', schema=None) as batch_op:
        stamp_item_position = postgresql.ENUM('TOP', 'CENTER', 'BOTTOM', 'LEFT', 'RIGHT', name='stamp_item_position')
        stamp_item_position.create(bind=batch_op.get_bind())
        batch_op.add_column(sa.Column('position', stamp_item_position, nullable=True))
        batch_op.alter_column('type',
            existing_type=sa.VARCHAR(),
            nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('stamp_template_metadata', schema=None) as batch_op:
        batch_op.alter_column('type',
            existing_type=sa.VARCHAR(),
            nullable=True)
        batch_op.drop_column('position')

    # ### end Alembic commands ###
