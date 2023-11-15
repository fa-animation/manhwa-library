from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class manga_status(str, Enum):
  Current = "current"
  TBA = "tba"
  finished = "finished"
  Unreleased = "unreleased"
  Upcoming = "upcoming"

class manga_type(str, Enum):
  Manhwa = "manhwa"
  Manhua = "manhua"
  Manga = "manga"
  Novel = "novel"
  Oel = "oel"
  Oneshot = "oneshot"

class ManhwaBase(BaseModel):
  id: Optional[UUID] = None
  title: str
  slug: Optional[str] = None
  description: str
  status_progress: manga_status
  ratting: float
  image: str
  view_count: Optional[int] = None
  year_published: str
  type_book: manga_type
  created_at: Optional[datetime] = None
  update_at: Optional[datetime] = None

class Pagination(BaseModel):
  total: int

class ShowsSearch(BaseModel):
  pagination: Pagination
  data: List[ManhwaBase]
  class Config:
    from_attributes = True
    json_schema_extra = {
        "example": {
          "title": "Solo leveling",
          "description": "Solo Leveling, também traduzido alternativamente como Only I Level Up, é uma web novel sul-coreana escrita por Chugong.",
          "status_progress": "Ongoing",
          "ratting": 4.5,
          "image": "https://m.media-amazon.com/images/I/71gnuYUWeTL._AC_UF1000,1000_QL80_.jpg",
          "view_count": 100,
          "year_published": "2022",
          "author": "Chugong",
          "artist": "DUBU",
          "type_book": "manhwa"
      }
    }

class ManhwaNoList(BaseModel):
  data: ManhwaBase
  class Config:
    from_attributes = True
    json_schema_extra = {
        "example": {
          "title": "Solo leveling",
          "description": "Solo Leveling, também traduzido alternativamente como Only I Level Up, é uma web novel sul-coreana escrita por Chugong.",
          "status_progress": "Ongoing",
          "ratting": 4.5,
          "image": "https://m.media-amazon.com/images/I/71gnuYUWeTL._AC_UF1000,1000_QL80_.jpg",
          "view_count": 100,
          "year_published": "2022",
          "author": "Chugong",
          "artist": "DUBU",
          "type_book": "manhwa"
      }
    }