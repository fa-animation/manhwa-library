from fastapi import HTTPException, status
# from uuid import UUID
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func
from app.infra.models import models
from app.schemas.schema import *

from abc import ABC, abstractmethod

class Repository(ABC):
  @abstractmethod
  def getAll(self):
    pass

class RecommedRepositorio(Repository):
  
  def getAll(self, db: Session) -> Manhwa:
    getAllManhwa = db.query(models.ManhwaModel).order_by(func.random()).first()
    return getAllManhwa
  