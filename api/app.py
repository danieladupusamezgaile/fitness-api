from fastapi import FastAPI
from .utils.exercisesdb_crud import search_exercises, get_all_exercises_opt_search

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, World!"}

@app.get("/exercises")
async def get_all_exercises(offset = 0, limit = 10, search = "", sortBy = "targetMuscles", sortOrder = "desc"):
    results = await get_all_exercises_opt_search(params={
                "offset": offset,
                "limit": limit,
                "search": search,
                "sortBy": sortBy,
                "sortOrder": sortOrder
            })
    return results

@app.get("/exercises/search")
async def search(q: str, offset: int = 0, limit: int = 10, threshold: float = 0.3):
    results = await search_exercises(params={"q": q, "offset": offset, "limit": limit, "threshold": threshold})
    return results
