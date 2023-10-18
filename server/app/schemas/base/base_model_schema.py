from uuid import UUID
from pydantic import BaseModel
from typing import Union, Optional
from datetime import datetime

class PrudutoBase(BaseModel):
  id: Optional[UUID] = None
  nome: str
  detalhes: Union[str, None] = None
  preco: float
  disponivel: bool
  created_at: Optional[datetime] = None
