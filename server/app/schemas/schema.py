from .base import base_model_schema

class Manhwa(base_model_schema.ManhwaBase):
  """
    - id: Optional[UUID] = None
    - nome: str
    - detalhes: Union[str, None] = None
    - preco: float
    - disponivel: bool
    - created_at: Optional[datetime] = None
  """
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