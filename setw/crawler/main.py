import sys
import time
from loguru import logger

from setw.settings import get_settings
from setw.crawler.load import upload_file_to_s3
from setw.crawler.crawl import crawl
from setw.crawler.transform import transform
from setw.crawler.utils import generate_date_range

from setw.database.database import Database
from setw.database.stores import StockPrice as StockPriceStore

setting = get_settings()
twse = setting['twse']
export_file = setting['export_file']

url = twse['URL']
export_folder = export_file['FOLDER']
export_data_type = export_file['DATA_TYPE']


def main():
    start_date, end_date, *_ = sys.argv[1:]
    date_range = generate_date_range(start_date, end_date)

    try:
        logger.info('connect to database...')
        db = Database(
            uri='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4',
        )
        db.create_tables()
    except Exception:
        logger.error('Raise exception when creating tables.')
        raise

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

        try:
            logger.info('insert into database...')
            stock_price = StockPriceStore(db.session)
            df = df.head(2)
            stock_price.create_stock_prices(df.to_dict('records'))
        except Exception:
            logger.error('Raise exception when bulk inserting records.')
            raise


if __name__ == '__main__':
    main()
