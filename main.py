from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from book import Book, session

app = FastAPI()

class BookSchema(BaseModel):
    book_no:int
    book_name:str
    book_price:int
    book_color:str

    class Config:
        orm_mode = True

class updateBookSchema(BaseModel):
    book_no:Optional [int]
    book_name:Optional [str]
    book_price:Optional [int]
    book_color:Optional [str]
    

    class Config:
        orm_mode = True

@app.get('/')
def get_all_books() -> List[BookSchema]:
    books = session.query(Book).all()
    return books

@app.get('/books/{id}')
def get_one_book(id : int) -> BookSchema:
    single_book = session.query(Book).filter_by(book_no = id).first()
    return single_book



@app.patch('/books/update/{id}')
def update_book(id : int, payload: updateBookSchema) -> BookSchema:
    updated_detail = session.query(Book).filter_by(book_no = id).one()
    if not updated_detail:
        raise HTTPException(status_code = 404, detail = 'Book does does NOT exist in our DataBase')
    for key, value in payload.dict(exclude_unset = True).items():
        setattr(updated_detail, key, value)
    session.commit()
    return updated_detail

@app.put('/books/update/{id}')
def update_book(id : int, payload: BookSchema) -> BookSchema:
    updated_detail = session.query(Book).filter_by(book_no = id).one()
    if not updated_detail:
        raise HTTPException(status_code = 404, detail = 'Book does does NOT exist in our DataBase')
    for key, value in payload.dict(exclude_unset = True).items():
        setattr(updated_detail, key, value)
    session.commit()
    return updated_detail

@app.delete('/books/delete/{id}')
def delete_book(id : int) -> None:
    bk = session.query(Book).filter_by(book_no = id).first()
    session.delete(bk)
    session.commit()
    return{"detail": f'Book with id {id} deleted successfully'}

@app.post('/data')
def add_data(book: BookSchema) -> BookSchema:
    bk = Book(**dict(book))
    session.add(bk)
    session.commit()

    return book