# from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import desc
from sqlalchemy.sql.expression import func
from app.infra.models import models
from app.schemas.schema import *

from abc import ABC, abstractmethod

class Repository(ABC):
  @abstractmethod
  def get_all(self):
    pass
  @abstractmethod
  def get_tranding(self):
    pass
  @abstractmethod
  def search_manga(self, name):
    pass
  

class RecommedRepositorio(Repository):
  
  def get_all(self, db: Session) -> list[Manhwa]:
    return db.query(models.ManhwaModel).order_by(func.random()).first()
  
  def get_tranding(self, db: Session) -> list[Manhwa]:
    tranding = db.query(models.ManhwaModel).order_by(desc(models.ManhwaModel.view_count)).limit(10)

    return tranding.all()
  
  def search_manga(self, name: str,db: Session) -> list[Manhwa]:
    getAllManhwa = db.query(models.ManhwaModel).filter(models.ManhwaModel.title.like(name)).limit(15)
    return getAllManhwa.all()