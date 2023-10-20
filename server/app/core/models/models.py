import uuid
from sqlalchemy import Column, Uuid, DateTime, String, Float, Boolean
from sqlalchemy.sql import func
from app.core.database.connect import Base
from datetime import datetime

class Produto(Base):
  __tablename__ = 'manhwa'

  id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
  title = Column(String)
  description = Column(String)
  status = Column(String)
  note = Column(Float)
  link = Column(String)
  created_at = Column(DateTime(timezone=True), server_default=func.now(args=['utc']))