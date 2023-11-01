from fastapi import status, APIRouter, Response, Depends
from app.infra.core.database import connect
from sqlalchemy.orm import Session
from app.schemas.base.base_model_schema import ShowsSearch

from app.infra.repository import recommed_manhwa

manhwaRecommend = recommed_manhwa.RecommedRepositorio()
router = APIRouter(
  prefix="/search",
  tags=["search"],
)
@router.get("/search/", 
  status_code=status.HTTP_200_OK,
  response_model=ShowsSearch,
  summary="Pesquisar um manga especifico"
)
def get_search_manga(name: str, db: Session = Depends(connect.get_db)):
  name = "%{}%".format(name)
  show = manhwaRecommend.searchManga(name, db)
  response = {"data": show, 'pagination': {'total': len(show)}}
  return response
