from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from app.infra.models import models
from app.schemas.schema import base_model_schema as base

from abc import ABC, abstractmethod

class Repository(ABC):
  @abstractmethod
  def get_all(self, skip: int = 0, limit: int = 100):
    pass

  @abstractmethod
  def save(self, model):
    pass


class ChapterRepositorio(Repository):
  def get_all(self, db: Session, skip: int = 0, limit: int = 100):
    get_random = db.query(models.ChapterModel).offset(skip).limit(limit)
    return get_random.all()
  
  def save(self, chapter: base.CreateChapter, db: Session):
    manga_db = models.ChapterModel(**chapter.model_dump())
    try:
      db.add(manga_db)
      db.commit()
      db.refresh(manga_db)
      return manga_db
    except IntegrityError as err:
      db.rollback()
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail=f"{str(err)}" 
      )