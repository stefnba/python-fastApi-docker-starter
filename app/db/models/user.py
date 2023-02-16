from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from ..db import Base
from ..utils.model import model_representation



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    username = Column(String)
    is_active = Column(Boolean, default=True)

    # items = relationship("Item", back_populates="owner")

    def __repr__(self):
        return model_representation(self, id=self.id, username=self.username)


# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")