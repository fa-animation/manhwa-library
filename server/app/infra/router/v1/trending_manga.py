from fastapi import status, Depends
from fastapi.routing import APIRouter
from app.infra.core.database import connect
from sqlalchemy.orm import Session
from app.schemas.base.base_model_schema import ShowsSearch

from app.infra.repository import recommed_manhwa

manhwaRecommend = recommed_manhwa.RecommedRepositorio()

router = APIRouter()

@router.get("/manga/", 
  status_code=status.HTTP_200_OK,
  response_model=ShowsSearch,
  summary="Obter o top 10 mangas mais lidos"
)
def get_trending_manga(db: Session = Depends(connect.get_db)):
  show = manhwaRecommend.get_tranding(db)
  response = {"data": show, 'pagination': {'total': len(show), 'count': 1}}
  return response

