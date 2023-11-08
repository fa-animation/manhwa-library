# from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy import desc
from sqlalchemy.sql.expression import func
from app.infra.models import models
from app.schemas.schema import *

from abc import ABC, abstractmethod

class Repository(ABC):
  @abstractmethod
  def get_all(self, skip: int = 0, limit: int = 100):
    pass
  def get_one(self):
    pass
  @abstractmethod
  def get_tranding(self):
    pass
  @abstractmethod
  def search_manga(self, name):
    pass
  

class RecommedRepositorio(Repository):
  
  def get_one(self, db: Session) -> Manhwa:
    return db.query(models.ManhwaModel).order_by(func.random()).first()
  
  def get_all(self, db: Session, skip: int = 0, limit: int = 100) -> list[Manhwa]:
    get_random = db.query(models.ManhwaModel).order_by(func.random()).offset(skip).limit(limit)
    return get_random.all()
  
  def get_tranding(self, db: Session) -> list[Manhwa]:
    tranding = db.query(models.ManhwaModel).order_by(desc(models.ManhwaModel.view_count)).limit(10)

    return tranding.all()
  
  def search_manga(self, name: str,db: Session) -> list[Manhwa]:
    getAllManhwa = db.query(models.ManhwaModel).filter(models.ManhwaModel.title.like(name)).limit(18)
    return getAllManhwa.all()