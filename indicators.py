import pandas as pd


def SMA(window,closing_prices):
    return(pd.Series(closing_prices).rolling(window=window).mean())