# pylint: disable=no-member,missing-function-docstring,invalid-name
"""users

Revision ID: dc45bccc0049
Revises: 
Create Date: 2023-02-15 20:34:41.007141

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = 'dc45bccc0049'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(
		"""
			CREATE TABLE IF NOT EXISTS users (
                id SERIAL4 PRIMARY KEY,
                username varchar(255) NOT NULL,
                email varchar(255) NOT NULL,
                is_active BOOLEAN DEFAULT FALSE
            )
		"""
	)


def downgrade() -> None:
    op.execute(
		"""
			DROP TABLE IF EXISTS tessssst
		"""
	)
