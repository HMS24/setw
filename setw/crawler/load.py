from setw.database.database import Database
from setw.database.repositories import StockPriceRepository
from setw.database.services import StockPriceService

db = Database(
    uri='mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4',
)
db.create_tables()


def load_into_mysql(df):
    stock_price_service = StockPriceService(
        session_factory=db.session,
        repository_class=StockPriceRepository,
    )
    stock_price_service.create_stock_prices(df.head(3).to_dict('records'))
