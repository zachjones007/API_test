#https://stackoverflow.com/questions/71496730/fastapi-settings-dependency
### config.py
from pydantic import BaseSettings
class Settings(BaseSettings):
    VERSION: str
    OPENAPI_PREFIX: str
settings = Settings()

### main.py
from fastapi import FastApi
from .config import settings
app = FastAPI(
    title='projectX',
    description="my description",
    version=settings.VERSION,
    root_path=settings.OPENAPI_PREFIX,
    openapi_url="/openapi.json",
    prefix="/api"
) 
