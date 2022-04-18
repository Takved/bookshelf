import uvicorn
from fastapi import FastAPI

from app.models import Book as Book
from app.models import newBook as newBook
import app.bookshelf

from fastapi.responses import JSONResponse

api = FastAPI()

@api.get("/")
async def info():
    status = JSONResponse(status_code = 400, content={"message": "Use /bookshelf/ to access books on shelf"})
    return status

@api.get("/bookshelf/")
async def list_books():
    try:
        status = await app.bookshelf.db_list()
    except:
        status = JSONResponse(status_code = 400, content={"message": "DB connetction error"})
    return status

@api.post("/bookshelf/", response_model=newBook)
async def add_book(newbook : newBook):
    book = Book(id=None, title=newbook.title, genre=newbook.genre, author=newbook.author, deadline=newbook.deadline, readed=newbook.readed)
    try:
        status = await app.bookshelf.db_add(book)
    except:
        status = JSONResponse(status_code = 400, content={"message": "DB connetction error"})
    return status

@api.patch("/bookshelf/{title}")
async def mark_book(title : str):
    try:
        status = await app.bookshelf.db_mark(title)
    except:
        status = JSONResponse(status_code = 400, content={"message": "DB connetction error"})
    return status

@api.delete("/bookshelf/{title}")
async def delete_book(title : str):
    try:
        status = await app.bookshelf.db_del(title)
    except:
        status = JSONResponse(status_code = 400, content={"message": "DB connetction error"})
    return status

if __name__ == '__main__':
    uvicorn.run("api:api", port=8000, host='127.0.0.1')