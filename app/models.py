from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean

from pydantic import BaseModel, constr
from typing import Optional

Base = declarative_base()

#
# Model
#
class Book(Base):
    __tablename__ = "book"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    genre = Column(String, nullable=False)
    author = Column(String, nullable=False)
    deadline = Column(Integer)
    readed = Column(Boolean, default=False)

#
# Scheme
#
class newBook(BaseModel):
    title: constr(min_length=1)
    genre: str
    author: str
    deadline: int
    readed: Optional[bool] = False


    class Config:
        orm_mode = True
    