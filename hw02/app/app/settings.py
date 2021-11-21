from pydantic import BaseSettings, PostgresDsn


class Settings(BaseSettings):
    db_dsn: PostgresDsn


settings = Settings()
