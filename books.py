from fastapi import FastAPI

app = FastAPI()

BOOKS = [
    {
        "title": "The Great Gatsby",
        "author": "arif",
        "category": "Fiction",
        "pages": 180
    },
    {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "category": "Fiction",
        "pages": 281
    },
    {
        "title": "1984",
        "author": "arif",
        "category": "Dystopian",
        "pages": 328
    },
    {
        "title": "A Brief History of Time",
        "author": "Stephen Hawking",
        "category": "Science",
        "pages": 212
    },
    {
        "title": "The Catcher in the Rye",
        "author": "arif",
        "category": "Fiction",
        "pages": 277
    },
    {
        "title": "The Lean Startup",
        "author": "Eric Ries",
        "category": "Business",
        "pages": 336
    },
    {
        "title": "Sapiens: A Brief History of Humankind",
        "author": "Yuval Noah Harari",
        "category": "History",
        "pages": 443
    },
    {
        "title": "Educated",
        "author": "Tara Westover",
        "category": "Memoir",
        "pages": 334
    },
    {
        "title": "Becoming",
        "author": "Michelle Obama",
        "category": "Biography",
        "pages": 426
    },
    {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "category": "Fiction",
        "pages": 208
    }
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.get("/books/{book_title}")
async def read_book(book_title: str):
    for book in BOOKS:
        if book.get("title").casefold() == book_title.casefold():
            return book
        

@app.get("/books/")
async def book_by_category(category: str):
    catList = []
    for book in BOOKS:
        if book.get("category").casefold() == category.casefold():
            catList.append(book)
    return catList    


@app.get("/books/{author}/")
async def bookListCatWithAut(author: str, category: str):
    catList = []
    for book in BOOKS:
        if book.get("author").casefold() == author.casefold() and book.get("category").casefold() == category.casefold():
            catList.append(book)
    return catList        