from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class Status(Enum):
  Ongoing = "Ongoing"
  Completed = "Completed"
  Finished = "Finished"
  Canceled = "Canceled"

class ManhwaBase(BaseModel):
  id: Optional[UUID] = None
  title: str
  slug: Optional[str] = None
  description: str
  status_progress: str
  ratting: float
  image: str
  view_count: Optional[int] = None
  year_published: str
  author: str
  artist: str
  created_at: Optional[datetime] = None

class ShowsSearch(BaseModel):
  length: int
  data: List[ManhwaBase]
  class Config:
    from_attributes = True

class ManhwaNoList(BaseModel):
  data: ManhwaBase
  class Config:
    from_attributes = True