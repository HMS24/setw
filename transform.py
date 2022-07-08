from pandas import DataFrame
from mapping import zh_en_map
from type_schemas import TaiwanStockExchange


def _translate_columns_languages(columns, mapper):
    return [mapper[col] for col in columns]


def _cast_type(df, type_schema):
    df_dict = df.to_dict('records')
    casted = [type_schema(**item).__dict__ for item in df_dict]

    return DataFrame(casted)


def transform(df, date):
    df = df.copy()
    df.columns = _translate_columns_languages(df.columns, zh_en_map)

    df['dir'] = (df['dir']
                 .str.split('>')
                 .str[1]
                 .str[0])
    df['change'] = df['dir'] + df['change'].astype(str)
    df = df.drop('dir', axis=1)

    # note: 價格相關，例如開盤價會有 '--' 代表無意義數值，為了存資料庫並且計算方便 replace 為 '0'，
    # 所有 col 先 to_str ，後續一起轉成對應的 type
    for col in df.columns:
        df[col] = (df[col]
                   .astype(str)
                   .str.strip()
                   .str.replace(',', '')
                   .str.replace('X', '')
                   .str.replace('--', '0'))

    df = df.fillna('')
    df['date'] = date
    df = _cast_type(df, TaiwanStockExchange)

    return df
