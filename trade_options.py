from pybit import HTTP
import json


# add api keys to this

session = HTTP("https://api.bybit.com",
               api_key="", api_secret="")


def long_(amount, price):
    # send buy to trading platform
    session.place_active_order(
        symbol="BTCUSD",
        side="Buy",
        order_type="Market",
        qty=amount,
        time_in_force="GoodTillCancel"
    )


def short(amount, price):
    # send sell to trading platform
    session.place_active_order(
        symbol="BTCUSD",
        side="Sell",
        order_type="Market",
        qty=amount,
        time_in_force="GoodTillCancel"
    )


def position_info():
    session.my_position(
        symbol="BTCUSD"
    )


def last_trade_closed():
    return (session.closed_profit_and_loss(symbol="BTCUSD"))
