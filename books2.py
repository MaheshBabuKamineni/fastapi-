from fastapi import FastAPI

app = FastAPI()

Books = []


@app.get("/books")
async def read_all_books():
    return Books



