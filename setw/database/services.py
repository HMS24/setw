class StockPriceService:

    def __init__(self, session_factory, repository_class):
        self._session_factory = session_factory
        self._repository_class = repository_class

    def create_stock_prices(self, stock_prices):
        with self._session_factory() as session:
            repository = self._repository_class(session)
            repository.bulk_insert(stock_prices)
            session.commit()
