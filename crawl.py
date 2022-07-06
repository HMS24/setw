from datetime import datetime
import requests
import pandas as pd

from mapping import zh_en_map

RESP_DATA_TYPE = 'json'
CRAWL_TYPE = 'ALLBUT0999'
BASE_URL = 'https://www.twse.com.tw'
LANGUAGE = 'zh'


def generate_headers(referer=None):
    return {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "www.twse.com.tw",
        "Referer": referer,
        "sec-ch-ua": '" Not;A Brand";v="99", "Microsoft Edge";v="103", "Chromium";v="103"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "macOS",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36 Edg/103.0.1264.37",
        "X-Requested-With": "XMLHttpRequest",
    }


def translate_columns_languages(columns, mapper):
    return [mapper[col] for col in columns]


def crawl(url, headers):
    resp = requests.get(url=url, headers=headers)
    result = resp.json()

    try:
        data = result['data9']
        columns = result['fields9']
    except KeyError:
        data = result.get('data8', [])
        columns = result.get('fields8', [])

    columns = translate_columns_languages(columns, zh_en_map)

    return pd.DataFrame(data=data, columns=columns)


def main():
    now = datetime.now()
    # date_str = now.date().strftime('%Y%m%d')
    timestamp_milliseconds = int(now.timestamp() * 1000)

    url = f'{BASE_URL}/{LANGUAGE}/exchangeReport/MI_INDEX?response={RESP_DATA_TYPE}&type={CRAWL_TYPE}&date={20220704}&_={timestamp_milliseconds}'
    headers = generate_headers(
        referer=f'{BASE_URL}/{LANGUAGE}/page/trading/exchange/MI_INDEX.html'
    )

    df = crawl(url, headers)


if __name__ == '__main__':
    main()
