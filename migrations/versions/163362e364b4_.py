"""empty message

Revision ID: 163362e364b4
Revises: 
Create Date: 2023-05-22 18:04:17.909385

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '163362e364b4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('matricula',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellido', sa.String(length=50), nullable=False),
    sa.Column('facultad', sa.String(length=50), nullable=False),
    sa.Column('jornada', sa.String(length=50), nullable=False),
    sa.Column('modalidad', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('registro',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre', sa.String(length=50), nullable=False),
    sa.Column('apellido', sa.String(length=50), nullable=False),
    sa.Column('correo', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('registro')
    op.drop_table('matricula')
    # ### end Alembic commands ###