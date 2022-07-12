from setw.database.models import StockPrice as StockPriceModel


class StockPrice:

    def __init__(self, session_factory):
        self.session_factory = session_factory

    def create_stock_prices(self, stock_prices):
        with self.session_factory() as session:
            session.bulk_insert_mappings(StockPriceModel, stock_prices)
            session.commit()
