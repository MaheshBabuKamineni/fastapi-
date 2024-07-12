from fastapi import FastAPI, Body

app = FastAPI()

Books = []


@app.get("/books")
async def read_all_books():
    return Books

@app.post("/createbooks")
async def create_all_books(book_request = Body()):
    return Books.append(book_request)




