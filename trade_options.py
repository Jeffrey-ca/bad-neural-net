from pybit import HTTP
import urllib.request
# TODO add code for this
url = "https://api.nomics.com/v1/currencies/ticker?key=eac98628bdb9380063b206ccfc5f3725dcc621bb&ids=BTC&interval=1d&per-page=100&page=1"
a = (urllib.request.urlopen(url).read())

file = open("btc_data.txt", "wb")
file.write(a)
file = open("btc_data.txt", "rb")


# Price * Available balance * leverage * percentage * (1-(0.00075*2))

'''price = 
balance = 
'''


def usd_to_perc(leverage, percentage):
    return(price * balance * 2 * leverage * percentage * (1-(0.00075*2)))


def long():
    # send buy to trading platform
    print('long')


def short():
    # send sell to trading platform
    print('short')


def close():
    # send close position to platform
    print('close')
