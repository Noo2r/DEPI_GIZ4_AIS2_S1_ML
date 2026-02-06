import pandas as pd

class Functions:
    """
    This class contains functions to check the data types and unique values
    as well as to check the null values and their ratios.
    """

    def __init__(self):
        pass

    def chk(self, df):
        dtypes = df.dtypes
        n_unique = df.nunique()
        return pd.DataFrame({'dtypes': dtypes, 'n_unique': n_unique})

    def chk_nulls(self, df):
        nulls = df.isnull().sum()
        ratio = nulls / len(df) * 100
        return pd.DataFrame({'Null': nulls,'Ratio': ratio})

    def convert_to_category(self, df, cols):
        df[cols] = df[cols].astype('category')
        return self.chk(df)

