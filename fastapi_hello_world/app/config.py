from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "FastAPI Hello World"
    DEBUG: bool = True

    class Config:
        env_file = ".env"

settings = Settings()
