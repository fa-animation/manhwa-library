from fastapi import status, Depends
from fastapi.routing import APIRouter
from app.infra.core.database import connect
from sqlalchemy.orm import Session
from app.schemas.base.base_model_schema import ShowsSearch

from app.infra.repository import recommed_manhwa

manhwaRecommend = recommed_manhwa.RecommedRepositorio()
router = APIRouter()
@router.get("/", 
  status_code=status.HTTP_200_OK,
  response_model=ShowsSearch,
  summary="Pesquisar um manga pelo titulo"
)
def get_search_manga(name: str, db: Session = Depends(connect.get_db)):
  name = f"%{name}%"
  show = manhwaRecommend.search_manga(name, db)
  response = {"data": show, 'pagination': {'total': len(show)}}
  return response
