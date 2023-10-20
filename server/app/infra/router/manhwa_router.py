from typing import List
from uuid import UUID
from fastapi import status, APIRouter, Response, HTTPException, Depends
from sqlalchemy.orm import Session
#importações locais
from app.infra.core.database import connect
from app.schemas.schema import Manhwa
from app.infra.repository import manhwa_repository

manhwaRepo = manhwa_repository.ManhwaRepositorio()

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Manhwa], summary="Obter todos os manhwa")
def getAllManhwa(db: Session = Depends(connect.get_db)):
  """
  Obter todos os manhwa do banco de dados.

  Retorna:
    - List[Manhwa]: Uma lista de todos os manhwa.
  """
  return manhwaRepo.getAll(db)

@router.get("/last", status_code=status.HTTP_200_OK, response_model=List[Manhwa], summary="Obter os manhwa mais recentes")
def getLastManhwa(db: Session = Depends(connect.get_db)):
  """
  Obter o ultimo manhwa do banco de dados.

  Retorna:
    - Manhwa: O objeto `Manhwa` com o `id` correspondente.
  """
  return manhwaRepo.getLast(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Manhwa, summary="Obter um manhwa por ID")
def getManhwaById(id: UUID, db: Session = Depends(connect.get_db)):
  """
  Buscar um manhwa pelo id (GET)

  Parameters:
    - id (UUID): O ID do manhwa a ser atualizado.
  
  Raises:
    - HTTPException: Se o manhwa com o ID especificado não for encontrado.

  Returns:
    - manhwa: O manhwa recuperado.
  """
  manhwaId = manhwaRepo.getById(id, db)
  if not manhwaId:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Obra não encontrado com esse id: {id}")
  return manhwaId

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Manhwa, summary="Criar um novo manhwa")
def createManhwa(manhwa: Manhwa, db: Session = Depends(connect.get_db)):
  """
  Criar (POST) um novo manhwa.

  Returns:
    - manhwa (Manhwa): Manhwa criado.
  """
  return manhwaRepo.save(manhwa, db)

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Manhwa, summary="Atualizar um produto")
def updateManhwa(id: UUID, manhwa: Manhwa, db: Session = Depends(connect.get_db)):
  """
  Atualiza (PUT) um manhwa com o ID especificado.

  Parameters:
    - id (UUID): O ID do manhwa a ser atualizado.
    - manhwa (manhwa): O objeto de manhwa atualizado.

  Raises:
    - HTTPException: Se o manhwa com o ID especificado não for encontrado.
      
  Returns:
    - manhwa: O manhwa atualizado.
  """
  item_content = manhwaRepo.getById(id, db)
  if not item_content:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Obra não encontrado com esse id: {id}")
  updated_user = manhwaRepo.update(item_content, manhwa, db)
  return updated_user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Excluir um manhwa")
def deleteManhwa(id: UUID, db: Session = Depends(connect.get_db)):
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