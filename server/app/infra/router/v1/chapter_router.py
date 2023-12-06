from fastapi import status, APIRouter, Depends
from sqlalchemy.orm import Session
#importações locais
from app.infra.core.database import connect
from app.schemas.base.base_model_schema import ShowsSearch
from app.schemas.schema import base_model_schema as base
from app.infra.repository.chapter_manhwa import chapter


chapterManhwa = chapter.ChapterRepositorio()

router = APIRouter()
@router.get("/", 
  status_code=status.HTTP_200_OK, 
)
def get_chapter(skip: int | None = 0, limit: int | None = 12,db: Session = Depends(connect.get_db)):
  response = chapterManhwa.get_all(db, skip=skip, limit=limit)
  # response = {'data': show, 'pagination': {'total': len(show)}}
  return response

@router.post("/", 
  status_code=status.HTTP_201_CREATED, 
  response_model=base.ChapterListData, 
)
def post_chapter(chapter: base.CreateChapter ,db: Session = Depends(connect.get_db)):
  """
  Obter as recomendações de manga do banco de dados.
  """
  show = chapterManhwa.save(chapter, db)
  response = {'data': show }
  return response