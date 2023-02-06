from fastapi import FastAPI

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
