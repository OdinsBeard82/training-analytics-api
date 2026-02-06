from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "training-analytics-api"
    ENV: str = "development"    
    DATABASE_URL: str 

settings = Settings()
