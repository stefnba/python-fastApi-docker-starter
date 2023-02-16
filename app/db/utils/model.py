from ..db import Base

def model_representation(model: Base, **kwargs):
    items = []
    for key, value in kwargs.items():
        item = f"{key}=\"{value}\""
        items.append(item)
    return f"<{model.__class__.__name__} ({', '.join(items)})>"