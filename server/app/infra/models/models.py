import uuid
from sqlalchemy import Column, Uuid, DateTime, String, Float, Boolean
from sqlalchemy.sql import func
from app.infra.core.database.connect import Base

class ManhwaModel(Base):
  __tablename__ = 'manhwa'

  id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
  title = Column(String)
  slug = Column(String)
  description = Column(String)
  status_progress = Column(String)
  ratinting = Column(Float)
  image = Column(String)
  view_count = Column(Float)
  year_published = Column(String)
  author = Column(String)
  artist = Column(String)
  created_at = Column(DateTime(timezone=True), server_default=func.now(args=['utc']))