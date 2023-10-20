from typing import Union, Optional
from uuid import UUID
from enum import Enum
from pydantic import BaseModel
from datetime import datetime

# class Status(Enum):
#   Ongoing = "Ongoing"
#   Completed = "Completed"
#   Finished = "Finished"
#   Canceled = "Canceled"

class ManhwaBase(BaseModel):
  id: Optional[UUID] = None
  title: str
  slug: Optional[str] = None
  description: str
  status_progress: str
  ratting: float
  image: str
  view_count: Optional[float] = None
  year_published: str
  author: str
  artist: str
  created_at: Optional[datetime] = None
