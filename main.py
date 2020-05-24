from robinhood_util import get_data, get_client
import pandas as pd

if __name__ == "__main__":
    print("start")

    rh_client = get_client()

    interesting_stocks = ["NVDA", "MSFT", "SQQQ", "SDOW"]
    interesting_stocks_processed = {}

    for stock in interesting_stocks:
        current_data = get_data(rh_client, stock)
        current_processed_data = dict()

        current_processed_data['id'] = stock
        current_processed_data['ask_price'] = current_data['ask_price']
        # TODO: get all interesting columns (values) into a new dict instead of all data

        interesting_stocks_processed[stock] = current_processed_data

    df = pd.DataFrame.from_dict(interesting_stocks_processed, orient="index")

    # write a function that gets a dataframe and returns a dict
    # dict should have only one row
    # dict should have columns for interesting aggregations like mean (avg), min, max etc.

    # next stage - group stocks by categories, return stats by category
    # a little bit more advanced calculations and aggregations


    # get stock price data over time
    # save all the requested data locally
    # create a simple graph showing stock price

    # create flask application that shows stock price over time (and all the other cool lines)
    # show data in table

    # connect to real user

    # get actions/transactions




    # average_asking_price_a = df['ask_price'].astype('double').mean()
    # average_asking_price_b = pd.to_numeric(df['ask_price']).mean()
    #
    # print(f"the average asking price is {average_asking_price_a}")
    # print(f"the average asking price is {average_asking_price_b}")

    # instead of print ask price,

    print("done")
