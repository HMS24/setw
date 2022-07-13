import sys
import time
from loguru import logger

from setw.settings import get_settings
from setw.pipeline.crawl import crawl
from setw.pipeline.transform import transform
from setw.pipeline.load import load_into_mysql
from setw.pipeline.aws import upload_file_to_s3
from setw.pipeline.utils import generate_date_range

setting = get_settings()
twse = setting['twse']
export_file = setting['export_file']

url = twse['URL']
export_folder = export_file['FOLDER']
export_data_type = export_file['DATA_TYPE']


def main():
    start_date, end_date, *_ = sys.argv[1:]
    date_range = generate_date_range(start_date, end_date)

    for date in date_range:
        logger.info(f'crawl date: {date}...')
        time.sleep(10)

        filepath = f'{export_folder}/{date}.{export_data_type}'
        df = crawl(url, date)

        if df.empty:
            continue

        df = transform(df, date)
        df.to_csv(filepath, index=False)
        upload_file_to_s3(filepath)
        load_into_mysql(df)


if __name__ == '__main__':
    main()
