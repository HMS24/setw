from sqlalchemy.sql import func
from sqlalchemy import (
    Column,
    String,
    Integer,
    BigInteger,
    Numeric,
    Date,
    DateTime,
)

from setw.database.database import Base


class StockPrice(Base):

    __abstract__ = True

    stock_id = Column(String(16), primary_key=True)
    stock_name = Column(String(16), nullable=False)
    trade_volume = Column(Integer, nullable=False)
    transaction = Column(Integer, nullable=False)
    trade_value = Column(BigInteger, nullable=False)
    opening_price = Column(Numeric(8, 2), nullable=False)
    highest_price = Column(Numeric(8, 2), nullable=False)
    lowest_price = Column(Numeric(8, 2), nullable=False)
    closing_price = Column(Numeric(8, 2), nullable=False)
    change = Column(Numeric(8, 2), nullable=False)
    last_best_bid_price = Column(Numeric(8, 2), nullable=False)
    last_best_bid_volume = Column(Integer, nullable=False)
    last_best_ask_price = Column(Numeric(8, 2), nullable=False)
    last_best_ask_volume = Column(Integer, nullable=False)
    price_earning_ratio = Column(Numeric(8, 2), nullable=False)
    date = Column(Date, primary_key=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True),
                        server_default=func.now(),
                        onupdate=func.now(),
                        )
