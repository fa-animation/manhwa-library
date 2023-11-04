"""main file where api is started"""
from fastapi import FastAPI, status
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from app.infra.core.config.settings import settings
from app.infra.router import router
from .infra.core.database import connect
# from app.utils import population_database

app = FastAPI(
  title= settings.api_title,
  version= settings.api_version,
  description= settings.api_description,
  contact= {
    "name": settings.api_contact_name,
    "email": settings.api_contact_email
	},
  docs_url="/v1/docs",
  redoc_url="/v1/redoc",
  openapi_url="/v1/openapi.json"
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

@app.get("/", response_model=dict, status_code=status.HTTP_200_OK)
def hello_world() -> dict:
  """Redirect to /docs"""
  return { 
    "status": "success",
    "message": "Hello World!",
    "data": {
      "docs": "/v1/docs/",
      "manga": "/v1/manga/",
      "search": "/v1/search/"
    },
  }

app.include_router(router.api_router, prefix="/v1")