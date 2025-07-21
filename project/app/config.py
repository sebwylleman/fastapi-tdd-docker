import logging
from functools import lru_cache

from pydantic_settings import BaseSettings

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = False


@lru_cache
def getSettings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()
