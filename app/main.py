from fastapi import FastAPI

from .db.repo import Query

app = FastAPI()


@app.get("/")
def read_root():
    """
    Get root route
    """
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    """
    Get item route
    """
    return {"item_id": item_id}


@app.get("/users")
def get_users():
    """
    Get item route
    """
    users = Query.User.list()
    return users


@app.get("/users/add")
def add_user():
    """
    Get item route
    """
    users = Query.User.add({"is_active": True, "email": "stefa", "password": "asdf", "username": "df"})
    return users
