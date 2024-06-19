## chat gpt 사용해서 코드 작성 및 직접 코드 수정
# alembic/versions/initial_migration.py

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = 'initial'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String, unique=True, index=True), #직접 코드 작성
        sa.Column('email', sa.String, unique=True, index=True), #직접 코드 작성
        sa.Column('hashed_password', sa.String),    #직접 코드 작성
        #sa.Column('favorite_politicians', sa.String),
    )

    op.create_table(
        'politicians',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String, index=True),
        sa.Column('party', sa.String),
        sa.Column('constituency', sa.String),
        sa.Column('contact', sa.String),
        sa.Column('gender', sa.String),
        sa.Column('election_count', sa.String),
        sa.Column('election_method', sa.String),
        sa.Column('attendance', sa.Integer),
        sa.Column('building', sa.Integer),
        sa.Column('deposit', sa.Integer),
        sa.Column('car', sa.Integer),
        sa.Column('political_fund', sa.Integer),
        sa.Column('securities', sa.Integer),
        sa.Column('land', sa.Integer),
    )

    #op.create_table(
    #    'user_politicians',
    #    sa.Column('user_id', sa.Integer, sa.ForeignKey('users.id')),
    #    sa.Column('politician_id', sa.Integer, sa.ForeignKey('politicians.id')),
    #)

def downgrade():
    #op.drop_table('user_politicians')
    op.drop_table('politicians')
    op.drop_table('users')
