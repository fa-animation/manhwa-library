import uuid
from sqlalchemy import Column, Uuid, DateTime, String, Float, Integer
from sqlalchemy.sql import func
from app.infra.core.database.connect import Base

class ManhwaModel(Base):
    __tablename__ = 'manhwa'

    id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    title = Column(String)
    slug = Column(String, unique=True)
    description = Column(String)
    status_progress = Column(String)
    ratting = Column(Float)
    image = Column(String)
    view_count = Column(Float)
    year_published = Column(String)
    author = Column(String)
    artist = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now(args=['utc']))

class GeneroModel(Base):
    __tablename__ = 'genero'

    id = Column(Integer, primary_key=True, index=True)
    name_gender = Column(String)
