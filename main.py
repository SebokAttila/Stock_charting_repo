from data import data_fetch

def main():
    ##data_fetch.fetch_raw_data_from_api()
    ##data_fetch.get_clean_data_from_csv()

    dataframe = data_fetch.get_stock_data()

    print(dataframe)
    print(type(dataframe))
if __name__ == '__main__':
    main()