import requests
import os
from dotenv import load_dotenv
load_dotenv()

base_url = os.getenv('BASE_URL')

def search_exercises(params: dict):
    response = requests.get(
        f"{base_url}exercises/search",
        params=params
    )
    return response.json()
