migrate-up:
	alembic -c app/db/alembic.ini upgrade head

migrate-down:
	alembic -c app/db/alembic.ini downgrade base

migrate-create:
	alembic -c app/db/alembic.ini revision -m $(name)

migrate-history:
	alembic -c app/db/alembic.ini history

packages:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

dev:
	uvicorn app.main:app --reload