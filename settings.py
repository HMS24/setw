from pydantic import BaseSettings


class Settings(BaseSettings):
    AWS_ACCOUNT_ID: str
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    AWS_S3_BUCKET_NAME: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings():
    return Settings().dict()
