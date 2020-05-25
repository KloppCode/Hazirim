from pyrh import Robinhood
from os import environ


def get_client():
    x = Robinhood()
    x.client_id = environ.get("RH_CLIENT_ID")
    x.refresh_token = environ.get("RH_REFRESH_TOKEN")
    x.device_token = environ.get("RH_DEVICE_TOKEN")
    x.username = environ.get("RH_USERNAME")
    x.password = environ.get("RH_PASSWORD")
    x.login(x.username, x.password)

    return x


def get_data(client, symbol):
    return client.get_quote(symbol)

def get_historical_data(client, symbol,interval,span):
    return client.get_historical_quotes(symbol,interval,span)

