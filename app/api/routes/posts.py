from typing import List
from fastapi import APIRouter

router = APIRouter()


@router.get("/")
async def get_all() -> List[dict]:
    posts = [
        {"id": 1, "title": "Olá Mundo!", "body": "Este é o meu primeiro post..."},
        {"id": 2, "title": "Acho que gostei...", "body": "Este é o meu segundo post..."},
    ]

    return posts
