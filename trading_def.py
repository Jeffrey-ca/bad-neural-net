from pybit import HTTP
from neural_net import *
import pickle

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
    return (session.my_position(symbol="BTCUSD"))


def last_trade_closed():
    return (session.closed_profit_and_loss(symbol="BTCUSD"))


# automatic labeling of previous trades
def auto_label_last():
    last_trade = last_trade_closed()
    pnl = last_trade["result"]["data"][0]["closed_pnl"]
    long_short = last_trade["result"]["data"][0]["side"]
    print(int(pnl*100000000))
    if long_short == "Buy":
        if int(pnl*100000000) > 1000:
            out[len(inp.keys())-1] = [-.8]
        elif int(pnl*100000000) <= 1000 and int(pnl*100000000) >= 250:
            out[len(inp.keys())-1] = [-.5]
        elif int(pnl*100000000) < 250 and int(pnl*100000000) > -250:
            out[len(inp.keys())-1] = [0]
        elif int(pnl*100000000) <= -250 and int(pnl*100000000) >= -1000:
            out[len(inp.keys())-1] = [.5]
        elif int(pnl*100000000) < -1000:
            out[len(inp.keys())-1] = [.8]
    if long_short == "Sell":
        if int(pnl*100000000) > 1000:
            out[len(inp.keys())-1] = [.8]
        elif int(pnl*100000000) >= 250 and int(pnl*100000000) <= 1000:
            out[len(inp.keys())-1] = [.5]
        elif int(pnl*100000000) < 250 and int(pnl*100000000) > -250:
            out[len(inp.keys())-1] = [0]
        elif int(pnl*100000000) <= -250 and int(pnl*100000000) >= -1000:
            out[len(inp.keys())-1] = [-.5]
        elif int(pnl*100000000) < -1000:
            out[len(inp.keys())-1] = [-.8]
    pickle_out2 = open('outputs.pickle', 'wb')
    pickle.dump(out, pickle_out2)
    pickle_out2.close()


# Converts webhooks into arrays for neural net to use
def array(request_json, X):
    if request_json["alert"] == '1m':
        X[0] = float(request_json["0"]) / 100
        X[1] = float(request_json["1"]) / 100
        X[2] = float(request_json["2"]) / 100
        X[3] = float(request_json["3"]) / 100
        if request_json["4"] == 'null':
            X[4] = 0
        else:
            X[4] = float(request_json["4"]) / 100
        if request_json["5"] == 'null':
            X[5] = 0
        else:
            X[5] = float(request_json["5"]) / 100
        if request_json["6"] == 'null':
            X[6] = 0
        else:
            X[6] = float(request_json["6"]) / 100
        X[7] = float(request_json["7"]) / 100000
        X[8] = float(request_json["8"]) / 100000
        X[9] = float(request_json["9"]) / 100000
        X[10] = float(request_json["10"]) / 100000
        X[11] = float(request_json["11"]) / 100000000
    if request_json["alert"] == '12m':
        X[12] = float(request_json["12"]) / 100
        X[13] = float(request_json["13"]) / 100
        X[14] = float(request_json["14"]) / 100
        X[15] = float(request_json["15"]) / 100
        if request_json["16"] == 'null':
            X[16] = 0
        else:
            X[16] = float(request_json["16"]) / 100
        if request_json["17"] == 'null':
            X[17] = 0
        else:
            X[17] = float(request_json["17"]) / 100
        if request_json["18"] == 'null':
            X[18] = 0
        else:
            X[18] = float(request_json["18"]) / 100
    if request_json["alert"] == '1hr':
        X[19] = float(request_json["19"]) / 100
        X[20] = float(request_json["20"]) / 100
        X[21] = float(request_json["21"]) / 100
        X[22] = float(request_json["22"]) / 100
        if request_json["23"] == 'null':
            X[23] = 0
        else:
            X[23] = float(request_json["23"]) / 100
        if request_json["24"] == 'null':
            X[24] = 0
        else:
            X[24] = float(request_json["24"]) / 100
        if request_json["25"] == 'null':
            X[25] = 0
        else:
            X[25] = float(request_json["25"]) / 100
    if request_json["alert"] == '4hr':
        X[26] = float(request_json["26"]) / 100
        X[27] = float(request_json["27"]) / 100
        X[28] = float(request_json["28"]) / 100
        X[29] = float(request_json["29"]) / 100
        if request_json["30"] == 'null':
            X[30] = 0
        else:
            X[30] = float(request_json["30"]) / 100
        if request_json["31"] == 'null':
            X[31] = 0
        else:
            X[31] = float(request_json["31"]) / 100
        if request_json["32"] == 'null':
            X[32] = 0
        else:
            X[32] = float(request_json["32"]) / 100
    if request_json["alert"] == '1d':
        X[33] = float(request_json["33"]) / 100
        X[34] = float(request_json["34"]) / 100
        X[35] = float(request_json["35"]) / 100
        X[36] = float(request_json["36"]) / 100
        if request_json["37"] == 'null':
            X[37] = 0
        else:
            X[37] = float(request_json["37"]) / 100
        if request_json["38"] == 'null':
            X[38] = 0
        else:
            X[38] = float(request_json["38"]) / 100
        if request_json["39"] == 'null':
            X[39] = 0
        else:
            X[39] = float(request_json["39"]) / 100
    pickle_out6 = open('X.pickle', 'wb')
    pickle.dump(X, pickle_out6)
    pickle_out6.close()
    return X


# Saves inputs and outputs of neural net
def save_in_out(array2):
    inp[len(inp.keys())] = array2
    pickle_out = open('inputs.pickle', 'wb')
    pickle.dump(inp, pickle_out)
    pickle_out.close()
    out_default = [0]
    out[len(inp.keys())] = out_default
    pickle_out2 = open('outputs.pickle', 'wb')
    pickle.dump(out, pickle_out2)
    pickle_out2.close()
