from pydantic import BaseSettings, BaseModel


class TaiwanStockExchange(BaseModel):
    HOST = 'www.twse.com.tw'
    REFERER = f'https://{HOST}/zh/page/trading/exchange/MI_INDEX.html'

    __BASE_URL = f'https://{HOST}'
    __LANGUAGE = 'zh'
    __RESP_TYPE = 'json'
    __CONTENT_TYPE = 'ALLBUT0999'

    URL = f'{__BASE_URL}/{__LANGUAGE}/exchangeReport/MI_INDEX'
    PARAMS = {
        'response': __RESP_TYPE,
        'type': __CONTENT_TYPE,
    }


class ExportFile(BaseModel):
    FOLDER = 'archives'
    DATA_TYPE = 'csv'


class BaseHeaders(BaseModel):
    HEADERS = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5',
        'Connection': 'keep-alive',
        'DNT': '1',
        'sec-ch-ua': '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': 'macOS',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37',
        "X-Requested-With": 'XMLHttpRequest',
    }


class Settings(BaseSettings):
    AWS_ACCOUNT_ID: str
    AWS_ACCESS_KEY: str
    AWS_SECRET_KEY: str
    AWS_S3_BUCKET_NAME: str

    twse:  TaiwanStockExchange = TaiwanStockExchange()
    base_headers: BaseHeaders = BaseHeaders()
    export_file:  ExportFile = ExportFile()

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'


def get_settings():
    return Settings().dict()
