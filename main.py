from flask import Flask, request, abort
from trade_options import *
from neural_net import *
from flask_ngrok import run_with_ngrok
import json

app = Flask(__name__)
run_with_ngrok(app)

@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        amount = 50
        amountx2 = amount * 2
        variable_sl_tp = 500
        price = int(round((request_json["7"])))
        X = array(request.json)
        out = output(X)
        save_in_out(X, output(X))
        trade = 0
        pos = 0
        if out[0] > 0.5 and trade == 0:
            long_(amount, price, variable_sl_tp)
            trade += 1
        if out[1] > 0.5 and trade == 0:
            short(amount, price, variable_sl_tp)
            trade -= 1
        if out[0] > 0.5 and trade != 0 and pos != 1:
            long_(amount2x, price, variable_sl_tp)
            pos = 1
        if out[1] > 0.5 and trade != 0 and pos != -1:
            short(amount2x, price, variable_sl_tp)
            pos = -1
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
