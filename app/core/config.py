from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "training-analytics-api"
    ENV: str = "development"
    DATABASE_URL: str

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
