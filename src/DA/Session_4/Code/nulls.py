import pandas as pd

def chk_nulls(df):
    nulls = df.isnull().sum()
    ration = nulls / len(df) * 100
    return pd.DataFrame({'Null': nulls, 'Ratio': ration}). T