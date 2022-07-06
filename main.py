from crawl import crawl, generate_headers
from load import upload_file
from settings import get_settings

setting = get_settings()
twse = setting['twse']
export = setting['export']

url = twse['URL']
params = twse['PARAMS']
date_str = params['date']
export_folder = export['FOLDER']
export_data_type = export['DATA_TYPE']


def main():
    df = crawl(url, params=params, headers=generate_headers())

    filepath = f'{export_folder}/{date_str}.{export_data_type}'
    df.to_csv(filepath, index=False)

    upload_file(filepath)


if __name__ == '__main__':
    main()
