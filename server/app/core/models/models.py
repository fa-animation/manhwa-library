import uuid
from sqlalchemy import Column, Uuid, DateTime, String, Float, Boolean
from sqlalchemy.sql import func
from app.core.database.connect import Base
from datetime import datetime

class Produto(Base):
  __tablename__ = 'produto'

  id = Column(Uuid(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
  nome = Column(String)
  detalhes = Column(String)
  preco = Column(Float)
  disponivel = Column(Boolean)
  created_at = Column(DateTime(timezone=True), server_default=func.now(args=['utc']))