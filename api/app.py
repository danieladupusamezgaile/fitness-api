from fastapi import FastAPI
from .utils.exercisesdb_crud import search_exercises

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/exercises/search")
async def search(q: str, offset:int = 0, limit: int = 10, threshold: float = 0.3):
    results = await search_exercises(params={"q": q, "offset": offset, "limit": limit, "threshold": threshold})
    return results
