"""add stamp and document tables

Revision ID: 698d135736b4
Revises: e38601fd2416
Create Date: 2025-04-02 22:17:17.342212

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '698d135736b4'
down_revision = 'e38601fd2416'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('documents',
        sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(length=100), nullable=False),
        sa.Column('provider_document_id', sa.String(length=50), nullable=False),
        sa.Column('service_provider', postgresql.ENUM('PAYSTACK', 'GOOGLE', 'MICROSOFT', name='service_provider', create_type=False), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stamp_templates',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(length=30), nullable=False),
        sa.Column('description', sa.String(length=60), nullable=False),
        sa.Column('shape', sa.Enum('RECTANGLE', 'SQUARE', 'OVAL', 'CIRCLE', 'HEXAGON', 'TRIANGLE', 'STAR', name='stamp_shape'), nullable=False),
        sa.Column('path_reference', sa.String(length=100), nullable=False),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name')
    )
    op.create_table('stamp_template_metadata',
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('template_id', sa.String(), nullable=False),
        sa.Column('key', sa.Enum('NAME', 'ADDRESS', 'EMAIL', 'PHONE', 'TAGLINE', 'DATE', 'TIMESTAMP', 'ID', 'MISC', 'ROLE', name='stamp_template_key'), nullable=False),
        sa.Column('max_size', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['template_id'], ['stamp_templates.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stamps',
        sa.Column('color_code', sa.String(length=10), nullable=False),
        sa.Column('created_by', sa.String(), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('name', sa.String(length=30), nullable=False),
        sa.Column('status', postgresql.ENUM('ACT', 'INACT', 'SUSP', 'ARCH', 'FLG', name='status', create_type=False), nullable=False),
        sa.Column('template_id', sa.String(), nullable=False),
        sa.Column('template_content', postgresql.JSONB(), nullable=False),
        sa.Column('updated_on', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('updated_by', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['created_by'], ['users.id'], ),
        sa.ForeignKeyConstraint(['template_id'], ['stamp_templates.id'], ),
        sa.ForeignKeyConstraint(['updated_by'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stamp_audit_logs',
        sa.Column('actor_id', sa.String(), nullable=False),
        sa.Column('created_on', sa.TIMESTAMP(timezone=True), nullable=False),
        sa.Column('document_id', sa.String(), nullable=False),
        sa.Column('id', sa.String(), nullable=False),
        sa.Column('event', sa.Enum('CREATE', 'DELETE', 'EDIT', 'APPLY', 'VERIFY', 'REPORT', 'ASSIGN', 'UNASSIGN', 'GENERAL', name='stamp_event'), nullable=False),
        sa.Column('notes', sa.String(length=150), nullable=False),
        sa.Column('stamp_id', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['actor_id'], ['users.id'], ),
        sa.ForeignKeyConstraint(['document_id'], ['documents.id'], ),
        sa.ForeignKeyConstraint(['stamp_id'], ['stamps.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stamp_users',
        sa.Column('stamp_id', sa.String(), nullable=False),
        sa.Column('user_id', sa.String(), nullable=False),
        sa.ForeignKeyConstraint(['stamp_id'], ['stamps.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('stamp_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('stamp_users')
    op.drop_table('stamp_audit_logs')
    op.drop_table('stamps')
    op.drop_table('stamp_template_metadata')
    op.drop_table('stamp_templates')
    op.drop_table('documents')
    # ### end Alembic commands ###
