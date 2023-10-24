from app.infra.core.database import connect 
from app.infra.models.models import ManhwaModel
from .init_content import CONTENT
from slugify import slugify

def data_load():
  db = next(connect.get_db())
  if len(db.query(ManhwaModel).all()) == 0:
		
    try:
      for content in CONTENT:
        content['slug'] = slugify(content['title'])
        manhwa_db = ManhwaModel(**content)
        db.add(manhwa_db)
        db.commit()
        db.refresh(manhwa_db)
    except Exception as err:
      print(err)        
      db.rollback()