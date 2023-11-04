from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import desc
from .repository import Repository
from sqlalchemy.exc import IntegrityError
from app.infra.models import models
from app.schemas.schema import *

class MangaRepositorio(Repository):
  
  def getAll(self, db: Session, skip: int = 0, limit: int = 100, order: str = "id") -> list[Manhwa]:
    """
    #### Recupera todos os registros do banco de dados.

    Argumentos:
      - db (Session): A sessão do banco de dados.
      - skip Optional[int] = 0: O número de registros a serem ignorados.
      - limit Optional[int] = 100: O número máximo de registros a serem recuperados.
      - order Optional[str] = "id": O campo para ordenar os registros

    Retorna:
      - List[Manhwa]: retorna uma lista de manga
    """
    getAllManhwa = db.query(models.ManhwaModel).order_by(desc(order)).offset(skip).limit(limit)
    return getAllManhwa.all()

  def getById(self, slug: str, db: Session) -> Manhwa:
    """
    #### Recupera um objeto `manga` do banco de dados com base no `slug` fornecido.

    Argumentos:
      - db (Session): O objeto de sessão do banco de dados.

    Retorna:
      - manga: O objeto `manga` com o `slug` correspondente.
    """
    return db.query(models.ManhwaModel).where(models.ManhwaModel.slug == slug).first()
  
  def save(self, manhwa: Manhwa, db: Session) -> Manhwa:
    """
    #### Salva um manga no banco de dados.

    Argumentos:
      - manga (manga): Os dados do manga como um dicionário.
      - db (Session): O objeto de sessão do banco de dados.

    Retorna:
      - manga: O objeto manga salvo.

    Raise:
      - HTTPException: Se houver um erro de integridade durante a operação de salvamento.
    """
    manga_db = models.ManhwaModel(**manhwa.model_dump())
    try:
      db.add(manga_db)
      db.commit()
      db.refresh(manga_db)
      return manga_db
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
      - item_content (manga): O conteúdo do item a ser atualizado.
      - manga (manga): O objeto manga contendo as informações atualizadas.
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