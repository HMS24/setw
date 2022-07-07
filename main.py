from crawl import crawl
from load import upload_file
from settings import get_settings

setting = get_settings()
twse = setting['twse']
export_file = setting['export_file']

url = twse['URL']
params = twse['PARAMS']
date_str = params['date']
export_folder = export_file['FOLDER']
export_data_type = export_file['DATA_TYPE']


def main():
    df = crawl(url=url, params=params)

    filepath = f'{export_folder}/{date_str}.{export_data_type}'
    df.to_csv(filepath, index=False)

    upload_file(filepath)


if __name__ == '__main__':
    main()
