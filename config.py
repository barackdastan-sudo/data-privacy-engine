from pydantic_settings import BaseSettings
class Settings(BaseSettings):
    REDIS_URL: str = "redis://localhost:6379"
    AES_SECRET_KEY: str = "12345678901234567890123456789012"
get_settings = Settings()
