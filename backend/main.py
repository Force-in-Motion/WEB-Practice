
from fastapi import FastAPI
from hw_1.view.book import router as book_router
from hw_1.view.user import router as user_router
from hw_2.view.post import router as post_router

app = FastAPI()

app.include_router(book_router)
app.include_router(user_router)
app.include_router(post_router)




if __name__ == "__main__":
    import uvicorn 
    uvicorn.run("main:app", port=8000, reload=True)