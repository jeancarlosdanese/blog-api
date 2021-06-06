from fastapi import APIRouter
from app.api.routes.posts import router as posts_router

router = APIRouter()
router.include_router(posts_router, prefix="/posts", tags=["posts"])
