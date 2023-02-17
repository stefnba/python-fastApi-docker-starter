from pydantic import BaseModel
from datetime import datetime


class OrderBase(BaseModel):
    title: str
    description: str | None = None
    amount: int
    created_at: datetime
    shipped_at: datetime | None
    owner_id: int


class ItemCreate(OrderBase):
    pass


class Item(OrderBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True
