from typing import List, Optional

from pydantic import BaseSettings

class FastApiSettings(BaseSettings):

    FAPP_HOST: Optional[str] = "localhost"
    FAPP_PORT: Optional[int] = 8000
    FAPP_RELOAD: bool = True

    FAPP_MIDDLEWARE_ENABLE_BurteMiddleware: bool = False
    FAPP_MIDDLEWARE_ENABLE_CORSMiddleware: bool = True
    FAPP_MIDDLEWARE_CORS_ALLOW_ORIGINS: List[str] = ["*"]
    FAPP_MIDDLEWARE_CORS_ALLOW_METHODS: List[str] = ["*"]
    FAPP_MIDDLEWARE_CORS_ALLOW_HEADERES: List[str] = ["*"]

    DB_NAME: Optional[str]
    DB_USERNAME: Optional[str]
    DB_PASSWORD: Optional[str]
    DB_HOST: Optional[str]
    DB_PORT: Optional[str]


settings = FastApiSettings(_env_file="../config/.env")