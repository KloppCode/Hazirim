from robinhood_util import get_data, get_client,get_historical_data
import pandas as pd

if __name__ == "__main__":
    print("start")

    rh_client = get_client()

    interesting_stocks = ["FB","AAPL","AMZN","NFLX","GOOG","NVDA","MSFT","TSLA","FDX","TVIX","SQQQ","SDOW"]
    interesting_stocks_processed = {}

    for stock in interesting_stocks:
        current_data = get_data(rh_client, stock)
        current_processed_data = dict()

        # TODO: get all interesting columns (values) into a new dict instead of all data
        # Added price close and changes in price
        ask_price = pd.to_numeric(current_data['ask_price'])
        previous_close_price = pd.to_numeric(current_data['previous_close'])
        dollar_change = ask_price - previous_close_price
        percentage_change = (dollar_change / previous_close_price) * 100

        # Getting historical data
        current_historical_data = get_historical_data(rh_client, stock, "day", "5year")

        # Issue with dates - fixed, 253 trading days a year
        one_year = 0
        two_year = 253 - 1
        three_year = 253 * 2 - 2
        four_year = 253 * 3 - 3
        five_year = 253 * 4 - 4

        one_year_price = pd.to_numeric(current_historical_data['results'][0]['historicals'][five_year]['close_price'])
        two_year_price = pd.to_numeric(current_historical_data['results'][0]['historicals'][four_year]['close_price'])
        three_year_price = pd.to_numeric(current_historical_data['results'][0]['historicals'][three_year]['close_price'])
        four_year_price = pd.to_numeric(current_historical_data['results'][0]['historicals'][two_year]['close_price'])
        five_year_price = pd.to_numeric(current_historical_data['results'][0]['historicals'][one_year]['close_price'])


        current_processed_data['id'] = stock
        current_processed_data['Previous close'] = current_data['previous_close']
        current_processed_data['ask price'] = current_data['ask_price']
        current_processed_data['bid price'] = current_data['bid_price']
        current_processed_data['last price'] = current_data['last_trade_price']
        current_processed_data['Change in $'] = dollar_change
        current_processed_data['Change in %'] = percentage_change
        current_processed_data['1Y'] = one_year_price
        current_processed_data['2Y'] = two_year_price
        current_processed_data['3Y'] = three_year_price
        current_processed_data['4Y'] = four_year_price
        current_processed_data['5Y'] = five_year_price

        # nice print
        print(current_data['symbol'], "/", "Close price:", previous_close_price, "/ price:", "$", ask_price, "/ $",
              dollar_change, "/ %", percentage_change)
        print("1Y: ", one_year_price, "/ 2Y:", two_year_price, "/ 3Y:", three_year_price, "/ 4Y:", four_year_price,
              "/ 5Y:", five_year_price)

        interesting_stocks_processed[stock] = current_processed_data

    df = pd.DataFrame.from_dict(interesting_stocks_processed, orient="index")
    # Michael To do
    # write a function that gets a dataframe and returns a dict
    # dict should have only one row
    # dict should have columns for interesting aggregations like mean (avg), min, max etc.
    # 20D, 50D ,200D average
    # end

    # next stage - group stocks by categories, return stats by category
    # a little bit more advanced calculations and aggregations


    # get stock price data over time
    # save all the requested data locally
    # create a simple graph showing stock price

    # create flask application that shows stock price over time (and all the other cool lines)
    # show data in table

    # connect to real user

    # get actions/transactions




    #  average_asking_price_a = df['ask_price'].astype('double').mean()
    #  average_asking_price_b = pd.to_numeric(df['ask_price']).mean()
    #
    # print(f"the average asking price is {average_asking_price_a}")
    # print(f"the average asking price is {average_asking_price_b}")
    #
    # # instead of print ask price,
    print("done")

