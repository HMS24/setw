from setw.database.schemas import StockPriceSchema


class StockPriceModel(StockPriceSchema):

    __tablename__ = 'stock_prices'

    def __repr__(self):
        return f"""<StockPrice(
            {self.stock_id},
            {self.stock_name},
            {self.date},
        )>"""
