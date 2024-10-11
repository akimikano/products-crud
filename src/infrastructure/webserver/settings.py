from pathlib import Path
from typing import Any, Dict, List, Optional, Union, Callable, Type, Tuple

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SECRET_KEY: str = "SECRET_KEY"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    POSTGRES_DB: str = "products_db"
    DB_HOST: str = "localhost"
    DB_PORT: str = "5432"
    POSTGRES_USER: str = "products_admin"
    POSTGRES_PASSWORD: str = "products"

    class Config:
        env_file = "./.env"


settings = Settings()
