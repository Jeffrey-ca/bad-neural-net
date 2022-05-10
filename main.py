from flask import Flask, request, abort
from trade_options import *
from neural_net import *
from flask_ngrok import run_with_ngrok
import json


trade = 0
pos = 0
pickle_out4 = open('pos.pickle', 'wb')
pickle.dump(pos, pickle_out4)
pickle_out4.close()
pickle_out3 = open('trade.pickle', 'wb')
pickle.dump(trade, pickle_out3)
pickle_out3.close()


app = Flask(__name__)
run_with_ngrok(app)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        pickle_in3 = open('trade.pickle', 'rb')
        trade = pickle.load(pickle_in3)
        pickle_in4 = open('pos.pickle', 'rb')
        pos = pickle.load(pickle_in4)
        pickle_in2 = open('heldprice.pickle', 'rb')
        heldprice = pickle.load(pickle_in2)
        amount = 10
        variable_sl_tp = 300
        amountx2 = amount * 2
        price = int(round(float(request.json["7"])))
        X = array(request.json)
        out = output(X)
        print(output(X))
        if out[0] > 0.5 and trade == 0:
            long_(amount, price, variable_sl_tp)
            pos = 1
            trade += 1
            save_in_out(X, output(X))
            holdprice(price, variable_sl_tp)
            print('This should be first trade')
        elif out[1] > 0.5 and trade == 0:
            short(amount, price, variable_sl_tp)
            trade -= 1
            pos = -1
            save_in_out(X, output(X))
            holdprice(price, variable_sl_tp)
            print('This should be first trade')
        elif out[0] > 0.5 and trade != 0 and pos != 1:
            long_(amountx2, price, variable_sl_tp)
            pos = 1
            save_in_out(X, output(X))
            holdprice(price, variable_sl_tp)
            print('This should be after first trade')
        elif out[1] > 0.5 and trade != 0 and pos != -1:
            short(amountx2, price, variable_sl_tp)
            pos = -1
            save_in_out(X, output(X))
            holdprice(price, variable_sl_tp)
            print('This should be after first trade')
        if price < heldprice[0] and pos == 1:
            pos = 0
            trade = 0
        if price > heldprice[1] and pos == 1:
            pos = 0
            trade = 0
        if price > heldprice[1] and pos == -1:
            pos = 0
            trade = 0
        if price < heldprice[0] and pos == -1:
            pos = 0
            trade = 0
        pickle_out4 = open('pos.pickle', 'wb')
        pickle.dump(pos, pickle_out4)
        pickle_out4.close()
        pickle_out3 = open('trade.pickle', 'wb')
        pickle.dump(trade, pickle_out3)
        pickle_out3.close()
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
