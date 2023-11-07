from fastapi import status, APIRouter, Response, HTTPException, Depends
from slugify import slugify
from sqlalchemy.orm import Session
import random
#importações locais
from app.infra.core.database import connect
from app.schemas.schema import Manhwa
from app.schemas.base.base_model_schema import ShowsSearch, ManhwaNoList
from app.infra.repository import manga_repository

manga_repo = manga_repository.MangaRepositorio()

router = APIRouter()

@router.get("/", 
  status_code=status.HTTP_200_OK, 
  response_model=ShowsSearch, 
  summary="Obter todos os manga"
)
def get_show_all_manga(order_by: str | None = None, skip: int | None = 0, limit: int = 12, db: Session = Depends(connect.get_db)):
  """
  ## Obtenha todos os programas de manga.

  Argumentos:
    - order_by (str | None): O campo para ordenar os programas.
    - limit (int): O número máximo de programas a serem recuperados.
  
  Exemplo:
  ```bash
  curl GET http://localhost:8000/manga?order_by=created_at&limit=12
  ```
  Retorna:
    - data (`manga`): Os dados salvos no banco de dados.
  """
 
  show = manga_repo.getAll(db, skip=skip, limit=limit, order=order_by)
  response = {'data': show, 'pagination': {'total': len(show)}}
  return response

@router.get("/{slug}/detail/", 
  status_code=status.HTTP_200_OK, 
  response_model=ManhwaNoList, 
  summary="Obter detalhes de um manga pelo slug"
)
def get_show_by_slug(slug: str, db: Session = Depends(connect.get_db)):
  """
  ## Buscar um manga pelo slug (GET)

  Parameters:
    - slug (string): O slug do manga para buscar informações.
  
  Raises:
    - HTTPException: Se o manga com o slug especificado não for encontrado.

  Returns:
    - manga: O manga recuperado.
  """
  manhwaId = manga_repo.getById(slug, db)
  if not manhwaId:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND, 
      detail=f"Nehuma obra foi encontrada com o slug: {slug}"
    )
  show = {"data": manhwaId}
  return show

@router.post("/", 
  status_code=status.HTTP_201_CREATED, 
  response_model=ManhwaNoList, 
  summary="Criar um novo manga"
)
def create_manga(manhwa: Manhwa, db: Session = Depends(connect.get_db)):
  """
  ## Criar (POST) um novo manga.

  Returns:
    - manga (Manga): manga criado.
  """
  if manhwa.slug == None:
    manhwa.slug = slugify(manhwa.title)
  if manhwa.view_count == None:
    manhwa.view_count = random.randint(90, 200) * 10
  manhwa = manga_repo.save(manhwa, db)
  show = {"data": manhwa}
  return show

@router.put("/{slug}", 
  status_code=status.HTTP_200_OK, 
  response_model=ManhwaNoList,
  summary="Atualizar um manga"
)
def update_manhwa(slug: str, manhwa: Manhwa, db: Session = Depends(connect.get_db)):
  """
  ## Atualiza (PUT) um manga com o slug especificado.

  Parameters:
    - slug (string): O slug do manga a ser atualizado.
  
  Body:
    - manga (manga): O objeto de manga atualizado.

  Raises:
    - HTTPException: Se o manga com o slug especificado não for encontrado.
      
  Returns:
    - data (Manga): O manga atualizado.
  """
  item_content = manga_repo.getById(slug, db)
  if not item_content:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Obra não encontrado com esse id: {id}")
  manhwa.slug = slugify(manhwa.title)
  updated_user = manga_repo.update(item_content, manhwa, db)
  show = {"data": updated_user}
  return show

@router.delete("/{slug}", 
  status_code=status.HTTP_204_NO_CONTENT, 
  summary="Excluir um manga"
)
def delete_manga(slug: str, db: Session = Depends(connect.get_db)):
  """
  ## Exclui (DELETE) um manga da lista de manga.

  Parameters:
  - slug (string): O slug do manga a ser excluído.

  Raise:
  - HTTPException: Caso o manga não exista 404 (NOT FOUND)

  Returns:
  - Resposta com um código de status 204 (NO CONTENT).
  """
  item_content = manga_repo.getById(slug, db)
  if not item_content:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Obra não encontrado com esse slug: {slug}"
    )
  manga_repo.delete(item_content, db)
  return Response(status_code=status.HTTP_204_NO_CONTENT)
