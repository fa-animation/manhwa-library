"""Module Settings"""
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
  """arquivo que carrega todas as variáveis de ambiente.
  Esta classe contém as seguintes configurações:
    - *api_title:* O título da API.
    - *api_version:* A versão da API.
    - *api_description:* Uma descrição da API.
    - *api_contact_name:* O nome da pessoa de contato da API.
    - *api_contact_email:* O endereço de e-mail da pessoa de contato da API.

  Estas configurações são carregadas do arquivo `.env` por padrão.
  """
  api_title: str
  api_version: str
  api_description:str
  api_contact_name:str
  api_contact_email: str
  
  class Config:
    """Leitura do .env"""
    env_file = ".env"

settings = Settings()
