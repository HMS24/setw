from datetime import datetime

from settings import get_settings
from load import upload_file_to_s3
from crawl import crawl
from transform import transform

setting = get_settings()
twse = setting['twse']
export_file = setting['export_file']

url = twse['URL']
export_folder = export_file['FOLDER']
export_data_type = export_file['DATA_TYPE']


def main():
    # date = datetime.now().date().strftime('%Y%m%d')
    date = '20220706'
    filepath = f'{export_folder}/{date}.{export_data_type}'

    df = crawl(url, date)
    df.to_csv(filepath, index=False)
    upload_file_to_s3(filepath)
    df = transform(df, date)
    # to_rds


if __name__ == '__main__':
    main()
