from typing import List
from uuid import UUID
from fastapi import status, APIRouter, Response, HTTPException, Depends
from sqlalchemy.orm import Session
#importações locais
from app.core.database import connect
from app.schemas.schema import Produto
from app.core.repository import produto_repository

produtolistRepo = produto_repository.ProdutoRepositorio()

router = APIRouter()

@router.get("/", status_code=status.HTTP_200_OK, response_model=List[Produto], summary="Obter todos os produtos")
def getAllProdutos(db: Session = Depends(connect.get_db)):
  """
  Obter todos os produtos do banco de dados.

  Retorna:
    - List[Produto]: Uma lista de todos os produtos.
  """
  return produtolistRepo.getAll(db)

@router.get("/last", status_code=status.HTTP_200_OK, response_model=List[Produto], summary="Obter os produto mais recentes")
def getLastProduto(db: Session = Depends(connect.get_db)):
  """
  Obter o ultimo produto do banco de dados.

  Retorna:
    - Produto: O objeto `Produto` com o `id` correspondente.
  """
  return produtolistRepo.getLast(db)

@router.get("/{id}", status_code=status.HTTP_200_OK, response_model=Produto, summary="Obter um produto por ID")
def getProdutoById(id: UUID, db: Session = Depends(connect.get_db)):
  """
  Buscar um produto pelo id (GET)

  Parameters:
    - id (UUID): O ID do produto a ser atualizado.
  
  Raises:
    - HTTPException: Se o produto com o ID especificado não for encontrado.

  Returns:
    - Produto: O produto recuperado.
  """
  produtoId = produtolistRepo.getById(id, db)
  if not produtoId:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto não encontrado com esse id: {id}")
  return produtoId

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=Produto, summary="Criar um novo produto")
def createProduto(produto: Produto, db: Session = Depends(connect.get_db)):
  """
  Criar (POST) um novo Produto.

  Returns:
    - produto (Produto): O objeto Produto criado.
  """
  return produtolistRepo.save(produto, db)

@router.put("/{id}", status_code=status.HTTP_200_OK, response_model=Produto, summary="Atualizar um produto")
def updateProduto(id: UUID, produto: Produto, db: Session = Depends(connect.get_db)):
  """
  Atualiza (PUT) um produto com o ID especificado.

  Parameters:
    - id (UUID): O ID do produto a ser atualizado.
    - produto (Produto): O objeto de produto atualizado.

  Raises:
    - HTTPException: Se o produto com o ID especificado não for encontrado.
      
  Returns:
    - Produto: O produto atualizado.
  """
  item_content = produtolistRepo.getById(id, db)
  if not item_content:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Produto não encontrado com esse id: {id}")
  updated_user = produtolistRepo.update(item_content, produto, db)
  return updated_user

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, summary="Excluir um produto")
def deleteProduto(id: UUID, db: Session = Depends(connect.get_db)):
  """
  Exclui (DELETE) um produto da lista de produtos.

  Parameters:
  - id (UUID): O ID do produto a ser excluído.

  Raise:
  - HTTPException: Caso o produto não exista 404 (NOT FOUND)

  Returns:
  - Resposta com um código de status 204 (NO CONTENT).
  """
  item_content = produtolistRepo.getById(id, db)
  if not item_content:
    raise HTTPException(
      status_code=status.HTTP_404_NOT_FOUND,
      detail=f"Produto não encontrado com esse id: {id}"
    )
  produtolistRepo.delete(item_content, db)
  return Response(status_code=status.HTTP_204_NO_CONTENT)