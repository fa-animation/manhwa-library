"""main file where api is started"""
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse
from .config.settings import settings
from .core.router import produto_router
from .core.database import connect

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

@app.get("/", status_code=status.HTTP_308_PERMANENT_REDIRECT)
def redirect_docs() -> dict:
  """Redirect to /docs"""
  return RedirectResponse(url='/docs')

app.include_router(produto_router.router, prefix="/manhwa", tags=["/manhwa"])