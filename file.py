import pandas as pd

def parse_excel(*cols, date_col, file):
    column_list = list(cols)
    df = pd.read_excel(file, usecols=column_list)
    df[date_col] = df[date_col].astype(str)
    data = df.to_dict(orient='list')
    return data