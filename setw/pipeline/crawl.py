from datetime import datetime
import requests
import pandas as pd

from setw.settings import get_settings

setting = get_settings()
twse = setting['twse']
base_headers = setting['base_headers']

twse_host = twse['HOST']
twse_referer = twse['REFERER']


def _generate_headers(host=None, referer=None):
    headers = {**base_headers['HEADERS']}
    headers['Host'] = host
    headers['Referer'] = referer

    return headers


def _generate_params(date):
    params = {**twse['PARAMS']}
    params['date'] = date
    params['_'] = int(datetime.now().timestamp() * 1000)

    return params


def crawl(url, date):
    headers = _generate_headers(twse_host, twse_referer)
    params = _generate_params(date)

    resp = requests.get(url=url, params=params, headers=headers)
    result = resp.json()

    try:
        data = result['data9']
        columns = result['fields9']
    except KeyError:
        data = result.get('data8', [])
        columns = result.get('fields8', [])

    return pd.DataFrame(data=data, columns=columns)
