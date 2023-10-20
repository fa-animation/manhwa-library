from fastapi import HTTPException, status
from uuid import UUID
from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import desc
from .repository import Repository
from sqlalchemy.exc import IntegrityError
from app.infra.models import models
from app.schemas.schema import *

class ManhwaRepositorio(Repository):
  
  def getAll(self, db: Session, skip: int = 0, limit: int = 100) -> List[Manhwa]:
    """
    #### Recupera todos os registros do banco de dados.

    Argumentos:
      - db (Session): A sessão do banco de dados.
      - skip Optional[int] = 0: O número de registros a serem ignorados.
      - limit Optional[int] = 100: O número máximo de registros a serem recuperados.

    Retorna:
      - List[Manhwa]: Uma lista de Manhwa representando os registros recuperados.
    """
    getAllManhwa = db.query(models.ManhwaModel).offset(skip).limit(limit)
    return getAllManhwa.all()
  def getLast(self, db: Session) -> List[Manhwa]:
    """
    #### Recupera todos os registros do banco de dados.

    Argumentos:
      - db (Session): A sessão do banco de dados.

    Retorna:
      - List[Manhwa]: Uma lista de Manhwa representando os últimos registros recuperados.
    """    
    getLasteManhwa = db.query(models.ManhwaModel).order_by(desc(models.ManhwaModel.created_at))
    return getLasteManhwa.all()
  
  def getById(self, id: UUID, db:Session) -> Manhwa:
    """
    #### Recupera um objeto `Manhwa` do banco de dados com base no `id` fornecido.

    Argumentos:
      - id (UUID): O identificador único do objeto `Produto`.
      - db (Session): O objeto de sessão do banco de dados.

    Retorna:
      - Manhwa: O objeto `manhwa` com o `id` correspondente.
    """
    return db.query(models.ManhwaModel).filter(models.ManhwaModel.id == id).first()
  
  def save(self, manhwa: Manhwa, db: Session) -> Manhwa:
    """
    #### Salva um manhwa no banco de dados.

    Argumentos:
      - Manhwa (Manhwa): Os dados do Manhwa como um dicionário.
      - db (Session): O objeto de sessão do banco de dados.

    Retorna:
      - Manhwa: O objeto Manhwa salvo.

    Raise:
      - HTTPException: Se houver um erro de integridade durante a operação de salvamento.
    """
    manhwa_db = models.ManhwaModel(**manhwa.model_dump())
    try:
      db.add(manhwa_db)
      db.commit()
      db.refresh(manhwa_db)
      return manhwa_db
    except IntegrityError as err:
      db.rollback()
      raise HTTPException(
        status_code=status.HTTP_400_BAD_REQUEST, 
        detail=f"{str(err)}" 
      )

  def update(self, item_content: Manhwa, manhwa: Manhwa, db: Session) -> Manhwa:
    """
    #### Atualize o conteúdo do item com as informações do manhwa determinado.

    Argumentos:
      - item_content (Manhwa): O conteúdo do item a ser atualizado.
      - Manhwa (Manhwa): O objeto Manhwa contendo as informações atualizadas.
      - db (Session): O objeto de sessão para operações de banco de dados.

    Retorna:
      - item_content: o conteúdo atualizado do item.
    """
    #Exmplo:
    # item_content.nome = produto.nome
    # item_content.detalhes = produto.detalhes
    # item_content.preco = produto.preco
    # item_content.disponivel = produto.disponivel
    update_query = db.query(models.ManhwaModel).filter(models.ManhwaModel.id == item_content.id)
    update_query.update(manhwa.model_dump(exclude_unset=True))
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