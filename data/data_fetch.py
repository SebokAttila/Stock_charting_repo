import os

import pandas as pd
import requests
import dotenv

dotenv.load_dotenv()

API_KEY = os.getenv("ALPHA_VANTAGE_API_KEY")
BASE_URL = os.getenv("ALPHA_VANTAGE_BASE_URL")

csv_file_path = r'/\raw_data\OHLCV.csv'

def get_stock_data():
    try:
        return get_clean_data_from_csv()
    except:
        return fetch_raw_data_from_api()

def fetch_raw_data_from_api():
    url = f"{BASE_URL}query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={API_KEY}"
    response = requests.get(url)

    stock_data = response.json()

    stock_dataframe = pd.DataFrame.from_dict(stock_data["Time Series (Daily)"], orient="index", dtype=float)

    stock_dataframe.reset_index(inplace=True)
    stock_dataframe.rename(columns={'index':'Date'}, inplace=True)

    stock_dataframe.to_csv(os.path.join("data", "../raw_data/OHLCV.csv"), index=False)

    return stock_dataframe

def get_clean_data_from_csv():
    stock_dataframe = pd.read_csv(os.path.join("data", "../raw_data/OHLCV.csv"))

    return stock_dataframe