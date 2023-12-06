import uuid
from sqlalchemy import Column, Uuid, DateTime, String, Float, Integer, ForeignKey, Table
from sqlalchemy.sql import func
from app.infra.core.database.connect import Base
from sqlalchemy.orm import relationship

# association_table
# association_table = Table(
#   "association_table",
#   Base.metadata,
#   Column("manhwa_id", ForeignKey("manhwa.id"), primary_key=True),
#   Column("category_id", ForeignKey("category.id"), primary_key=True),
# )

# class User(Base):
#   __tablename__ = 'users'
#   id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
#   name = Column(String)
#   username = Column(String, unique=True)
#   email = Column(String, unique=True)
#   password = Column(String)
#   role = Column(String, default='user')

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

  chapter = relationship("ChapterModel", back_populates="manhwa_relation", cascade="delete, delete-orphan")
  # category = relationship(
  #   "CategoryModel", secondary=association_table, back_populates="manhwa"
  # )
  created_at = Column(DateTime(timezone=True), server_default=func.now())
  update_at = Column(DateTime(timezone=True), onupdate=func.now())

# One (manga) To Many (chapter)

class ChapterModel(Base):
  __tablename__ = 'chapter'
  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  description = Column(String)
  image = Column(String)
  manhwa_id = Column(Uuid(as_uuid=True), ForeignKey("manhwa.id"))
  manhwa_relation = relationship("ManhwaModel", back_populates="chapter")

# Many To Many
# class CategoryModel(Base):
#   __tablename__ = 'category'
#   id = Column(Integer, primary_key=True, index=True)
#   name = Column(String)
#   manhwa = relationship(
#     "ManhwaModel", secondary=association_table, back_populates="category"
#   )
