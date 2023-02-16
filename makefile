migrate-up:
	alembic -c src/db/alembic.ini upgrade head

migrate-down:
	alembic -c src/db/alembic.ini downgrade base

migrate-create:
	alembic -c src/db/alembic.ini revision -m $(name)

migrate-history:
	alembic -c src/db/alembic.ini history

packages:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

dev:
	uvicorn app.main:app --reload