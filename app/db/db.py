import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from .utils.connection import connection_url_postgresql

load_dotenv()

host = os.environ.get("DB_HOST", "localhost")
port = os.environ.get("DB_PORT", 5432)
database = os.environ.get("DB_NAME")
user = os.environ.get("DB_ADMIN_USER")
password = os.environ.get("DB_ADMIN_PASSWORD")

engine = create_engine(
    connection_url_postgresql(host=host, port=port, database=database, user=user, password=password)
)

DBSession = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
