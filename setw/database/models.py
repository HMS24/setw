from setw.database.schemas import StockPrice as StockPriceSchema


class StockPrice(StockPriceSchema):

    __tablename__ = 'stock_prices'

    def __repr__(self):
        return f"""<StockPrice(
            {self.stock_id},
            {self.stock_name},
            {self.date},
        )>"""
