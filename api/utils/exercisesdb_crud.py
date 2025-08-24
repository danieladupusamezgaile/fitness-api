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
        response.raise_for_status()
        return response.json()
