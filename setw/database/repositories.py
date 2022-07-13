from setw.database.models import StockPriceModel


class StockPriceRepository:

    def __init__(self, session):
        self._session = session

    def bulk_insert(self, stock_prices):
        self._session.bulk_insert_mappings(StockPriceModel, stock_prices)
