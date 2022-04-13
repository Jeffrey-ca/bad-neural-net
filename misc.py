import ccxt
import ast


def parse_webhook(webhook_data):
    data = ast.literal_eval(webhook_data)
    return data




#unfinished need exchange
#def send_order(data):
 #   exchange = ccxt.