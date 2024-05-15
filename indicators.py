import pandas as pd

#SMA - simple moving average is calculated as taking the average of the past n closing prices
#      ie: if n/window is 5, will take the average of the first 5 days hence plot on the 6th
def SMA(window,closing_prices):
    return(pd.Series(closing_prices).rolling(window=window).mean())