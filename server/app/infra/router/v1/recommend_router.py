from fastapi import status, APIRouter,Depends
from sqlalchemy.orm import Session
#importações locais
from app.infra.core.database import connect
from app.schemas.base.base_model_schema import ManhwaNoList
from app.infra.repository import recommed_manhwa


manhwaRecommend = recommed_manhwa.RecommedRepositorio()

router = APIRouter()
@router.get("/random", 
  status_code=status.HTTP_200_OK, 
  response_model=ManhwaNoList, 
  summary="Obter as recomendações de manga",
)
def get_show_random_manga(db: Session = Depends(connect.get_db)):
  """
  Obter as recomendações de manga do banco de dados.
  """
  show = manhwaRecommend.get_all(db)
  response = {"data": show}
  return response
