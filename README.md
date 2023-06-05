# FastAPI Book API
This is a simple API built using FastAPI to manage book data. It allows you to perform CRUD operations on book objects.

## Installation
Clone the repository:
bash
Copy code
git clone <repository_url>
Install the dependencies using pip:
Copy code
pip install -r requirements.txt
Run the application:
css
Copy code
uvicorn main:app --reload
The API will be available at http://localhost:8000.

## Endpoints

GET /
Returns a list of all books.

GET /books/{id}
Returns details of a specific book identified by {id}.

PATCH /books/update/{id}
Updates the details of a specific book identified by {id}. You can provide any combination of optional fields (book_name, book_price, book_color) in the request body to update.

PUT /books/update/{id}
Updates the details of a specific book identified by {id}. You need to provide values for all fields (book_no, book_name, book_price, book_color) in the request body.

DELETE /books/delete/{id}
Deletes a specific book identified by {id}.

POST /data
Adds a new book to the database. You need to provide values for all fields (book_no, book_name, book_price, book_color) in the request body.

## Data Models

BookSchema
book_no (integer): The number of the book.
book_name (string): The name of the book.
book_price (integer): The price of the book.
book_color (string): The color of the book.

updateBookSchema
book_no (integer, optional): The updated engine number of the book.
book_name (string, optional): The updated name of the book.
book_price (integer, optional): The updated price of the book.
book_color (string, optional): The updated color of the book.
Database
The API uses a database to store book data. Make sure to configure the database connection in the book.py file.

## License
This project is licensed under the MIT License.
