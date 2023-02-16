# pylint: disable=missing-function-docstring
from sqlalchemy import select, insert, update
from typing import List, overload
# from ..schemas.user import UserCreate
from ..models.user import User
from ..utils.query import Query


class UserRepo:

    def add(self, data) -> User:
        ins = insert(User).returning(User)
        return Query.commit(ins, data)

    @overload
    def update(self, data: dict, id: int) -> User:
        ...

    @overload
    def update(self, data: List[dict], id: int) -> List[User]:
        ...
    def update(self, data, id: int) -> User | List[User]:
        return Query.commit(update(User).where(User.id == id).returning(User), data)

    def retrieve(self, id: int) -> User:
        return Query.one(select(User).where(User.id == id))

    def list(self) -> List[User]:
        return Query.many(select(User))
