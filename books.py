from fastapi import FastAPI, Body

app = FastAPI()

Books = [
    {'title': 'TitleOne', 'author': 'one', 'category': 'science'},
    {'title': 'TitleTwo', 'author': 'two', 'category': 'science'},
    {'title': 'TitleThree', 'author': 'three', 'category': 'science'},
    {'title': 'TitleFour', 'author': 'four', 'category': 'science'},
    {'title': 'TitleFive', 'author': 'five', 'category': 'science'}
]


@app.get("/")
async def read_all_books():
    return Books


@app.get("/books/{dynamic_param}")
async def read_book_by_param(dynamic_param: str):
    return {"dynamic_param": dynamic_param}


@app.get("/books/")
async def read_books_by_category(category: str):
    books_to_return = [book for book in Books if book.get("category").casefold() == category.casefold()]
    return books_to_return


@app.get("/books/{book_author}/")
async def read_books_by_categoryandauthor(book_author: str, category: str):
    books_to_return = []
    for books in Books:
        if books.get('author').casefold() == book_author().casefold() and \
                books.get('category').casefold() == category.casefold():
            books_to_return.append(books)
    return books_to_return


@app.post("/books/create_book")
async def read_create_book(new_book=Body()):
    Books.append(new_book)

