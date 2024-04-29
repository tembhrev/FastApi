from fastapi import Body, FastAPI

app = FastAPI()


class Book:
    id : int
    title: str
    author: str
    description: str
    rating:  int
    
    def __init__(self, id, title, author, description, rating):
        self.id = id
        self.title = title
        self.author = author
        self.description = description
        self.rating = rating
    
    
BOOKS = [
    Book(1, 'Computer Science Pro', 'codingwithlucky', 'A very nice book!', 5),
    Book(2, 'Be Fast with FastAPI', 'codingwithlucky', 'A great book!', 5),
    Book(3, 'Master Endpoints', 'codingwithlucky', 'A awesome book!', 5),
    Book(4, 'HP1', 'Author 1', 'Book Description', 2),
    Book(5, 'HP2', 'Author 2', 'Book Description', 3),
    Book(6, 'HP3', 'Author 3', 'Book Description', 1)
]

@app.get("/books")
async def read_all_books():
    return BOOKS

@app.post("/create-book")
async def create_book(book_request=Body()):
    BOOKS.append(book_request)