from setw.settings import get_settings
from setw.database.database import Database
from setw.database.repositories import StockPriceRepository
from setw.database.services import StockPriceService

settings = get_settings()
URI = settings.get('DATABASE_URI')

db = Database(URI)
db.create_tables()


def load_into_mysql(df):
    stock_price_service = StockPriceService(
        session_factory=db.session,
        repository_class=StockPriceRepository,
    )
    stock_price_service.create_stock_prices(df.to_dict('records'))
