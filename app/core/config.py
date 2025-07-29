from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str = "postgresql+asyncpg://postgres:postgres@postgres:5432/postgres"
    secret_key: str = "changeme"

    class Config:
        env_file = ".env"

settings = Settings()
