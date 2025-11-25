
from fastapi import FastAPI
from app.view.book import router as book_router
from app.view.user import router as user_router

app = FastAPI()

app.include_router(book_router)
app.include_router(user_router)




if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("main:app", port=8000, reload=True)