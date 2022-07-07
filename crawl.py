import requests
import pandas as pd

from settings import get_settings

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


def crawl(url, **kwargs):
    headers = _generate_headers(twse_host, twse_referer)
    resp = requests.get(url=url, headers=headers, **kwargs)
    result = resp.json()

    try:
        data = result['data9']
        columns = result['fields9']
    except KeyError:
        data = result.get('data8', [])
        columns = result.get('fields8', [])

    return pd.DataFrame(data=data, columns=columns)
