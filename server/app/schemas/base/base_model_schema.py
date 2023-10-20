from uuid import UUID
from pydantic import BaseModel
from typing import Union, Optional
from datetime import datetime
from enum import Enum

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
  ratinting: float
  image: str
  view_count: Optional[float] = None
  year_published: str
  author: str
  artist: str
  created_at: Optional[datetime] = None
