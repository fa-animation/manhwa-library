from fastapi import status, APIRouter, Response, HTTPException, Depends

from slugify import slugify
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
import random
#importações locais
from app.infra.core.database import connect
from app.schemas.schema import Manhwa
from app.schemas.base.base_model_schema import ShowsSearch, ManhwaNoList
from app.infra.repository import manhwa_repository, recommed_manhwa


manhwaRepo = manhwa_repository.ManhwaRepositorio()
manhwaRecommend = recommed_manhwa.RecommedRepositorio()

router = APIRouter()

@router.get("/", 
  status_code=status.HTTP_200_OK, 
  response_model=ShowsSearch, 
  summary="Obter todos os manhwa"
)
def get_show_all_manhwa(db: Session = Depends(connect.get_db)):
  """
  Obter todos os manhwa do banco de dados.

  Retorna:
    - Data[Manhwa]: Uma lista de todos os manhwa.
  """
  show = manhwaRepo.getAll(db)
  response = {'data': show, 'length': len(show)}
  return response

@router.get("/recommend", 
  status_code=status.HTTP_200_OK, 
  response_model=ManhwaNoList, 
  summary="Obter as recomendações de manhwa"
)
def get_show_recommend_manhwa(db: Session = Depends(connect.get_db)):
  """
  Obter as recomendações de manhwa do banco de dados.
  """
  show = manhwaRecommend.getAll(db)
  response = {"data": show}
  return response

@router.get("/last", 
  status_code=status.HTTP_200_OK, 
  response_model=ShowsSearch, 
  summary="Obter os manhwa mais recentes"
)
def get_show_last_manhwa(db: Session = Depends(connect.get_db)):
  """
  Obter o ultimo manhwa do banco de dados.

  Retorna:
    - Manhwa: O objeto `Manhwa` com o `id` correspondente.
  """
  show = manhwaRepo.getLast(db)
  response = {"data": show, "length": len(show)}
  return response

@router.get("/find/{slug}", 
  status_code=status.HTTP_200_OK, 
  response_model=ManhwaNoList, 
  summary="Obter um manhwa por ID"
)
def get_show_by_id(slug: str, db: Session = Depends(connect.get_db)):
  """
  Buscar um manhwa pelo id (GET)

  Parameters:
    - id (UUID): O ID do manhwa a ser atualizado.
  
  Raises:
    - HTTPException: Se o manhwa com o ID especificado não for encontrado.

  Returns:
    - manhwa: O manhwa recuperado.
  """
  manhwaId = manhwaRepo.getById(slug, db)
  if not manhwaId:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Obra não encontrado com esse id")
  show = {"data": manhwaId}
  return show

@router.post("/", 
  status_code=status.HTTP_201_CREATED, 
  response_model=ManhwaNoList, 
  summary="Criar um novo manhwa"
)
def create_manhwa(manhwa: Manhwa, db: Session = Depends(connect.get_db)):
  """
  Criar (POST) um novo manhwa.

  Returns:
    - manhwa (Manhwa): Manhwa criado.
  """
  if manhwa.slug == None:
    manhwa.slug = slugify(manhwa.title)
  if manhwa.view_count == None:
    manhwa.view_count = random.randint(90, 200) * 10
  manhwa = manhwaRepo.save(manhwa, db)
  show = {"data": manhwa}
  return show

@router.put("/find/{id}", 
  status_code=status.HTTP_200_OK, 
  response_model=ManhwaNoList,
  summary="Atualizar um produto"
)
def update_manhwa(id: str, manhwa: Manhwa, db: Session = Depends(connect.get_db)):
  """
  Atualiza (PUT) um manhwa com o ID especificado.

  Parameters:
    - id (UUID): O ID do manhwa a ser atualizado.
  
  Body:
    - manhwa (manhwa): O objeto de manhwa atualizado.

  Raises:
    - HTTPException: Se o manhwa com o ID especificado não for encontrado.
      
  Returns:
    - data (Manhwa): O manhwa atualizado.
  """
  item_content = manhwaRepo.getById(id, db)
  if not item_content:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Obra não encontrado com esse id: {id}")
  manhwa.slug = slugify(manhwa.title)
  updated_user = manhwaRepo.update(item_content, manhwa, db)
  show = {"data": updated_user}
  return show

@router.delete("/find/{id}", 
  status_code=status.HTTP_204_NO_CONTENT, 
  summary="Excluir um manhwa"
)
def delete_manhwa(id: UUID, db: Session = Depends(connect.get_db)):
  """
  Exclui (DELETE) um manhwa da lista de manhwas.

  Parameters:
  - id (UUID): O ID do manhwa a ser excluído.

  Raise:
  - HTTPException: Caso o manhwa não exista 404 (NOT FOUND)

  Returns:
  - Resposta com um código de status 204 (NO CONTENT).
  """
  item_content = manhwaRepo.getById(id, db)
  if not item_content:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Obra não encontrado com esse id: {id}"
    )
  manhwaRepo.delete(item_content, db)
  return Response(status_code=status.HTTP_204_NO_CONTENT)
