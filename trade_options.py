from pybit import HTTP
import urllib.request

#TODO add api commands for this whole page
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
