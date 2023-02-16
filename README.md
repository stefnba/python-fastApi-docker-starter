# python-fastApi-docker-starter

Starter template for Python 🐍 and FastAPI with Docker.

# Get Started

Run the following commands to create a virtual conda environment within the directory `.conda`, activate it and install packages listed in `requirements.txt`.

```console
conda create -p .conda python=3.10
conda activate "$PWD/.conda"
pip install -r requirements.txt
```

Start server

```console
uvicorn app.main:app --reload
```

Or

```console
make dev
```

# Database

## Migrations

Database migrations are done through [Alembic](https://alembic.sqlalchemy.org/en/latest/) and the [SQLAlchemy](https://www.sqlalchemy.org) engine. To simplify the commands, we use [Makefile](https://makefiletutorial.com).

Create a new migration file:

```bash
make migrate-create name=<name of migration file>
```

Run up migrations:

```bash
make migrate-up
```

Run down migrations:

```bash
make migrate-down
```
