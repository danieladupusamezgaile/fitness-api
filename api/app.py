from fastapi import FastAPI
from .utils.exercisesdb_crud import search_exercises

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/exercises/search")
async def search(q: str):
    results = await search_exercises(params={"q": q})
    return results
