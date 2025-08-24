import httpx
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

base_url = "https://exercises-db.vercel.app/api/v1/"

async def search_exercises(params: dict):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{base_url}exercises/search",
            params=params
        )
        return response.json()

async def get_all_exercises_opt_search(params: dict):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            url=f"{base_url}exercises",
            params=params
        )
        return response.json()
