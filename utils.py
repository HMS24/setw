import pandas as pd


def generate_date_range(start, end, date_format='%Y%m%d'):
    return pd.date_range(start, end).strftime(date_format)
