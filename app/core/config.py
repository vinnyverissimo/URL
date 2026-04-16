from pydantic_settings import BaseSettings, SettingsConfigDict

# app/core/config.py
class Settings(BaseSettings):
    DYNAMODB_URL: str
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_ACCESS_KEY: str
    AWS_REGION: str
    APP_NAME: str

    model_config = SettingsConfigDict(env_file=".env")

settings = Settings()