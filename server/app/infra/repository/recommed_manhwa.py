# from uuid import UUID
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import desc
from sqlalchemy.sql.expression import func
from app.infra.models import models
from app.schemas.schema import *

from abc import ABC, abstractmethod

class Repository(ABC):
  @abstractmethod
  def getAll(self):
    pass
  @abstractmethod
  def getTranding(self):
    pass
  @abstractmethod
  def searchManga(self, name):
    pass
  

class RecommedRepositorio(Repository):
  
  def getAll(self, db: Session) -> List[Manhwa]:
    getAllManhwa = db.query(models.ManhwaModel).order_by(func.random()).first()
    return getAllManhwa
  
  def getTranding(self, db: Session) -> List[Manhwa]:
    getAllManhwa = db.query(models.ManhwaModel).order_by(desc(models.ManhwaModel.view_count)).limit(10)

    return getAllManhwa.all()
  
  def searchManga(self, name: str,db: Session) -> List[Manhwa]:
    getAllManhwa = db.query(models.ManhwaModel).filter(models.ManhwaModel.title.like(name))
    return getAllManhwa.all()