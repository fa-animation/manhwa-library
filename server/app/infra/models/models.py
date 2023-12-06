import uuid
from sqlalchemy import Column, Uuid, DateTime, String, Float, Integer, ForeignKey
from sqlalchemy.sql import func
from app.infra.core.database.connect import Base
from sqlalchemy.orm import declarative_base, relationship


class ManhwaModel(Base):
  __tablename__ = 'manhwa'
  
  id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
  title = Column(String)
  slug = Column(String, unique=True)
  type_book = Column(String)
  description = Column(String)
  status_progress = Column(String)
  ratting = Column(Float)
  image = Column(String)
  view_count = Column(Integer)
  year_published = Column(String)

  chapter = relationship("ChapterModel", back_populates="manhwa_relation")

  created_at = Column(DateTime(timezone=True), server_default=func.now())
  update_at = Column(DateTime(timezone=True), onupdate=func.now())

# One (manga) To Many (chapter)

class ChapterModel(Base):
  __tablename__ = 'chapter'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  description = Column(String)
  image = Column(String)
  manhwa_id = Column(Integer, ForeignKey("manhwa.id"))
  manhwa_relation = relationship("ManhwaModel", back_populates="chapter")