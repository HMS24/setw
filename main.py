from datetime import datetime

from crawl import crawl, generate_headers
from load import upload_file

RESP_DATA_TYPE = 'json'
CRAWL_TYPE = 'ALLBUT0999'
BASE_URL = 'https://www.twse.com.tw'
LANGUAGE = 'zh'
EXPORT_FOLDER = 'resources'
EXPORT_DATA_TYPE = 'csv'


def main():
    now = datetime.now()
    # date_str = now.date().strftime('%Y%m%d')
    date_str = '20220705'
    timestamp_milliseconds = int(now.timestamp() * 1000)

    url = f'{BASE_URL}/{LANGUAGE}/exchangeReport/MI_INDEX?response={RESP_DATA_TYPE}&type={CRAWL_TYPE}&date={date_str}&_={timestamp_milliseconds}'
    headers = generate_headers(
        referer=f'{BASE_URL}/{LANGUAGE}/page/trading/exchange/MI_INDEX.html')

    df = crawl(url, headers)

    filepath = f'{EXPORT_FOLDER}/{date_str}.{EXPORT_DATA_TYPE}'
    df.to_csv(filepath, index=False)

    upload_file(filepath)


if __name__ == '__main__':
    main()
