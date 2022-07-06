from datetime import datetime
from pydantic import BaseSettings, BaseModel


class TaiwanStockExchange(BaseModel):
    BASE_URL = 'https://www.twse.com.tw'
    LANGUAGE = 'zh'
    RESP_TYPE = 'json'
    CONTENT_TYPE = 'ALLBUT0999'

    URL = f'{BASE_URL}/{LANGUAGE}/exchangeReport/MI_INDEX'
    PARAMS = {
        'response': RESP_TYPE,
        'type': CONTENT_TYPE,
        'date': '20220705',
        # 'date': datetime.now().date().strftime('%Y%m%d'),
        '_': int(datetime.now().timestamp() * 1000),
    }


class EXPORT(BaseModel):
    FOLDER = 'resources'
    DATA_TYPE = 'csv'


class Settings(BaseSettings):
    AWS_ACCOUNT_ID: str
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    AWS_S3_BUCKET_NAME: str

    twse:  TaiwanStockExchange = TaiwanStockExchange()
    export:  EXPORT = EXPORT()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings():
    return Settings().dict()
