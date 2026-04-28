import os.path

import pandas as pd
import yfinance as yf


def get_yahoo_data(symbol, start, end, interval):
    try:
        return get_historical_data_from_csv()
    except:
        return get_historical_data_from_api(symbol, start, end, interval)


def get_historical_data_from_api(symbol, start, end, interval):

    ticker = yf.Ticker(symbol)
    historical_dataframe = ticker.history(start=start, end=end, interval=interval)

    historical_dataframe.to_csv("C:/Users/Attila/PycharmProjects/Stock_charting_repo/raw_data/Yahoo_OHLCV_Hourly.csv")
    return historical_dataframe


def get_historical_data_from_csv():
    historical_dataframe = pd.read_csv( "C:/Users/Attila/PycharmProjects/Stock_charting_repo/raw_data/Yahoo_OHLCV_Hourly.csv")
    return historical_dataframe