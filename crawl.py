import requests
import pandas as pd


def generate_headers():
    return {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5",
        "Connection": "keep-alive",
        "DNT": "1",
        "Host": "www.twse.com.tw",
        "Referer": "https://www.twse.com.tw/zh/page/trading/exchange/MI_INDEX.html",
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


def crawl(url, **kwargs):
    resp = requests.get(url, **kwargs)
    result = resp.json()

    try:
        data = result['data9']
        columns = result['fields9']
    except KeyError:
        data = result.get('data8', [])
        columns = result.get('fields8', [])

    return pd.DataFrame(data=data, columns=columns)
