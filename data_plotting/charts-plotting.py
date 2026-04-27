import pandas as pd
import matplotlib.pyplot as plt
from data import data_fetch

def stock_plotting():

    stock_dataframe = data_fetch.get_stock_data()

    