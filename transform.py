from mapping import zh_en_map


def _translate_columns_languages(columns, mapper):
    return [mapper[col] for col in columns]


def transform(df, date):
    df = df.copy()
    df.columns = _translate_columns_languages(df.columns, zh_en_map)
    df['dir'] = (df['dir']
                 .str.split('>')
                 .str[1]
                 .str[0])

    df['change'] = df['dir'] + df['change'].astype(str)

    df['change'] = (df['change']
                    .str.strip()
                    .str.replace('X', '')
                    .astype(float))

    df = df.drop('dir', axis=1)

    for col in ('stock_id', 'stock_name'):
        df[col] = (df[col]
                   .astype(str)
                   .str.strip())

    for col in ('trade_volume', 'transaction', 'trade_value',
                'last_best_bid_volume', 'last_best_ask_volume'):
        df[col] = (df[col]
                   .astype(str)
                   .str.replace(',', '').
                   astype(int))

    # 價格部分 例如開盤價 會有 '--' 代表無意義
    # 為了存資料庫計算方便 replace 為 0.00
    for col in ('opening_price', 'highest_price', 'lowest_price',
                'closing_price', 'last_best_bid_price', 'last_best_ask_price',
                'price_earning_ratio'):
        df[col] = (df[col]
                   .astype(str)
                   .str.replace(',', '')
                   .str.replace('--', '0')
                   .astype(float))

    df = df.fillna('')
    df['date'] = date
    return df
