import httpx
import asyncio
import os
from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv('BASE_URL')

async def search_exercises(params: dict):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"{base_url}exercises/search",
            params=params
        )
        response.raise_for_status()
        return response.json()
