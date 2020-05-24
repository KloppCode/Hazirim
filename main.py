from robinhood_util import get_data, get_client

if __name__ == "__main__":
    print("start")

    rh_client = get_client()

    interesting_stocks = ["NVDA", "MSFT", "SQQQ", "SDOW"]
    interesting_stocks_processed = {}

    for stock in interesting_stocks:
        current_data = get_data(rh_client, stock)
        print(f"{stock}'s asking price is {current_data['ask_price']}")
        interesting_stocks_processed[stock] = current_data

    # something cool
    print("done")
