from typing import Optional, List
from uuid import UUID
from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class Status(str, Enum):
  Ongoing = "Ongoing"
  Completed = "Completed"
  Finished = "Finished"
  Canceled = "Canceled"

class Type_book(str, Enum):
  Manhwa = "manhwa"
  Manhua = "manhua"
  Manga = "manga"

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
  type_book: Optional[Type_book]
  created_at: Optional[datetime] = None

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