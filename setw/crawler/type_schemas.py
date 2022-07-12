from pydantic import BaseModel


class TaiwanStockExchange(BaseModel):
    stock_id: str
    stock_name: str
    trade_volume: int
    transaction: int
    trade_value: int
    opening_price: float
    highest_price: float
    lowest_price: float
    closing_price: float
    change: float
    last_best_bid_price: float
    last_best_bid_volume: int
    last_best_ask_price: float
    last_best_ask_volume: int
    price_earning_ratio: float
    date: str
