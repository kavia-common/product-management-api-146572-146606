from functools import lru_cache
from typing import List

from pydantic import AnyHttpUrl, BaseSettings, Field


class Settings(BaseSettings):
    """
    PUBLIC_INTERFACE
    Application settings using environment variables.

    Attributes:
        app_name (str): Name of the application.
        cors_allow_origins (List[str]): List of allowed origins for CORS.
        log_level (str): Log level for the application.
    """

    app_name: str = Field(default="Products Backend API", description="Application name")
    cors_allow_origins: List[AnyHttpUrl] | List[str] = Field(
        default=["*"],
        description="Allowed origins for CORS. Use '*' for all origins or provide specific origins.",
    )
    log_level: str = Field(default="INFO", description="Log level for the application")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache
def get_settings() -> Settings:
    """Resolve and cache settings instance."""
    return Settings()


# Singleton-like settings access
settings = get_settings()
