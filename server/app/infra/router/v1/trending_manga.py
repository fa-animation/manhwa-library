from fastapi import status, APIRouter, Response, Depends
from app.infra.core.database import connect
from sqlalchemy.orm import Session
from app.schemas.base.base_model_schema import ShowsSearch

from app.infra.repository import recommed_manhwa

manhwaRecommend = recommed_manhwa.RecommedRepositorio()

router = APIRouter(
  prefix="/trending",
  tags=["trending"],
)

@router.get("/manga/", 
  status_code=status.HTTP_200_OK,
  response_model=ShowsSearch,
  summary="Obter o top 10 mangas mais lidos"
)
def get_trending_manga(db: Session = Depends(connect.get_db)):
  show = manhwaRecommend.getTranding(db)
  response = {"data": show, 'pagination': {'total': len(show)}}
  return response
