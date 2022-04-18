import asyncio

from sqlalchemy import Column,  Integer, String, Boolean
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import select, update, delete
from fastapi.responses import JSONResponse

from app.models import Book as Book

DATABASE_URL = "postgresql+asyncpg://postgres:postgres@db/postgres"

engine = create_async_engine(DATABASE_URL , echo = True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession) # set expire_on_commit to true

async def db_list():
    async with async_session() as session:
        result = await session.execute(select(Book).order_by(Book.deadline.asc()))
        return result.scalars().all()

async def db_add(book : Book):
    async with async_session() as session:
        result = await session.execute(select(Book).where(Book.title == book.title))
        exist = result.scalars().first()
        if exist != None:
            answ =  JSONResponse(status_code = 400, content={"message": "Book already on shelf"})
        else:
            session.add(book)
            await session.commit()
            answ = book
        return answ

async def db_mark(title):
    async with async_session() as session:
        result = await session.execute(select(Book).where(Book.title == title))
        book = result.scalars().first()
        if book != None:
            book.readed = True
            await session.commit()
            answ = book
        else:
            answ = JSONResponse (status_code = 400, content={"message": "No book to mark"})
        return answ
        
async def db_del(title):
    async with async_session() as session:
        result = await session.execute(select(Book).where(Book.title == title))
        book = result.scalars().first()
        if book != None:
            await session.delete(book)
            await session.commit()
            answ = book
        else:
            answ = JSONResponse (status_code = 400, content={"message": "No book to delete"})
        return answ
