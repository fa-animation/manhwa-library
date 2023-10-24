"""main file where api is started"""
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.infra.core.config.settings import settings
from .infra.router import manhwa_router
from .infra.core.database import connect
from app.utils import population_database

app = FastAPI(
  title= settings.api_title,
  version= settings.api_version,
  description= settings.api_description,
  contact= {
    "name": settings.api_contact_name,
    "email": settings.api_contact_email
	}
)

app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],
  allow_credentials=True,
  allow_methods=["*"],
  allow_headers=["*"],
)

connect.create_database()
# population_database.data_load()

@app.get("/", status_code=status.HTTP_308_PERMANENT_REDIRECT)
def redirect_docs() -> dict:
  """Redirect to /docs"""
  return RedirectResponse(url='/docs')

app.include_router(manhwa_router.router, prefix="/manhwa", tags=["/manhwa"])