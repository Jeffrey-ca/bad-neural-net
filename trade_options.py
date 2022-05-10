from pybit import HTTP
import json

# TODO add api commands for this whole page
# Price * Available balance * leverage * percentage * (1-(0.00075*2))

'''price = 
balance = 
'''
# add api keys to this

session = HTTP("https://api.bybit.com",
               api_key="", api_secret="")



def usd_to_perc(leverage, percentage):
    return(price * balance * 2 * leverage * percentage * (1-(0.00075*2)))


def long_(amount, price, sl_tp):
    # send buy to trading platform
    session.place_active_order(
        symbol="BTCUSD",
        side="Buy",
        order_type="Market",
        qty=amount,
        take_profit=price+sl_tp,
        stop_loss=price-sl_tp,
        time_in_force="GoodTillCancel"
    )
    print('long')


def short(amount, price, sl_tp):
    # send sell to trading platform
    session.place_active_order(
        symbol="BTCUSD",
        side="Sell",
        order_type="Market",
        qty=amount,
        take_profit=price-sl_tp,
        stop_loss=price+sl_tp,
        time_in_force="GoodTillCancel"
    )
    print('short')


def close():
    # send close position to platform
    print('close')

# use this to turn incoming data from bybit into json file then read json file for price data & do this for balance on account too so percentage can be turned into usd


# I don't know why this isnt working
'''y = session.latest_information_for_symbol(
    symbol="BTCUSD"
)

with open('data.json', 'w') as fp:
    json.dump(y, fp)

f = open('data.json')
data = json.load(f)


for key, value in data.items():
    price = value['last_price']
    print(price)'''
