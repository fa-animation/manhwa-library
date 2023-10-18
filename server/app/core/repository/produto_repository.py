from uuid import UUID
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import desc
from fastapi import HTTPException, status
from .repository import Repository
from sqlalchemy.exc import IntegrityError
from app.core.models import models
from app.schemas.schema import *

class ProdutoRepositorio(Repository):
  
  def getAll(self, db: Session, skip: int = 0, limit: int = 100) -> List[Produto]:
    """
    #### Recupera todos os registros do banco de dados.

    Argumentos:
      - db (Session): A sessão do banco de dados.
      - skip Optional[int] = 0: O número de registros a serem ignorados.
      - limit Optional[int] = 100: O número máximo de registros a serem recuperados.

    Retorna:
      - List[Produto]: Uma lista de Produto representando os registros recuperados.
    """
    getAllProduto = db.query(models.Produto).offset(skip).limit(limit)
    return getAllProduto.all()
  def getLast(self, db: Session) -> List[Produto]:
    """
    #### Recupera todos os registros do banco de dados.

    Argumentos:
      - db (Session): A sessão do banco de dados.

    Retorna:
      - List[Produto]: Uma lista de Produto representando os últimos registros recuperados.
    """    
    getLastedProduto = db.query(models.Produto).order_by(desc(models.Produto.created_at))
    return getLastedProduto.all()
  
  def getById(self, id: UUID, db:Session) -> Produto:
    """
    #### Recupera um objeto `Produto` do banco de dados com base no `id` fornecido.

    Argumentos:
      - id (UUID): O identificador único do objeto `Produto`.
      - db (Session): O objeto de sessão do banco de dados.

    Retorna:
      - Produto: O objeto `Produto` com o `id` correspondente.
    """
    return db.query(models.Produto).filter(models.Produto.id == id).first()
  
  def save(self, produto: Produto, db: Session) -> Produto:
    """
    #### Salva um produto no banco de dados.

    Argumentos:
      - produto (Produto): Os dados do produto como um dicionário.
      - db (Session): O objeto de sessão do banco de dados.

    Retorna:
      - Produto: O objeto produto salvo.

    Raise:
      - HTTPException: Se houver um erro de integridade durante a operação de salvamento.
    """
    produto_db = models.Produto(**produto.model_dump())
    try:
      db.add(produto_db)
      db.commit()
      db.refresh(produto_db)
      return produto_db
    except IntegrityError as err:
      db.rollback()
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail=f"{str(err)}" 
      )

  def update(self, item_content: Produto, produto: Produto, db: Session) -> Produto:
    """
    #### Atualize o conteúdo do item com as informações do produto determinado.

    Argumentos:
      - item_content (Produto): O conteúdo do item a ser atualizado.
      - produto (Produto): O objeto produto contendo as informações atualizadas.
      - db (Session): O objeto de sessão para operações de banco de dados.

    Retorna:
      - item_content: o conteúdo atualizado do item.
    """
    # item_content.nome = produto.nome
    # item_content.detalhes = produto.detalhes
    # item_content.preco = produto.preco
    # item_content.disponivel = produto.disponivel
    update_query = db.query(models.Produto).filter(models.Produto.id == item_content.id)
    update_query.update(produto.model_dump(exclude_unset=True))
    # model_dump(): returns a dictionary of the model's fields and values. See Serialization.
    db.commit()
    return item_content

  def delete(self, item_content, db: Session):
    """
    #### Exclui um item do banco de dados.

    Argumentos:
      - item_content: O item a ser excluído.
      - db (Session): O objeto de sessão para operações de banco de dados.

    Retorna:
      - O item excluído.
    """
    db.delete(item_content)
    db.commit()
    return item_content