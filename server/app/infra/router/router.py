from fastapi.routing import APIRouter
from .v1 import manga_router, recommend_router, search_router, trending_manga, chapter_router

api_router = APIRouter()

api_router.include_router(trending_manga.router, prefix="/trending", tags=["trending"])
api_router.include_router(manga_router.router, prefix="/manga", tags=["manga"])
api_router.include_router(chapter_router.router, prefix="/chapter", tags=["chapter"])
api_router.include_router(search_router.router, prefix="/search", tags=["search"])
api_router.include_router(recommend_router.router, prefix="/recommend", tags=["recommend"])