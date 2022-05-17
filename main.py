from flask import Flask, request, abort
from trade_options import *
from neural_net import *
from flask_ngrok import run_with_ngrok
import json


reset()

app = Flask(__name__)
run_with_ngrok(app)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        pickle_in5 = open('webhook.pickle', 'rb')
        webhook = pickle.load(pickle_in5)
        pickle_in6 = open('X.pickle', 'rb')
        X = pickle.load(pickle_in6)
        request_json = request.json
        if request_json["alert"] == '1m' and webhook[0] == 0:
            X = array(request_json, X)
            webhook[0] = 1
        if request_json["alert"] == '12m' and webhook[1] == 0:
            X = array(request_json, X)
            webhook[1] = 1
        if request_json["alert"] == '1hr' and webhook[2] == 0:
            X = array(request_json, X)
            webhook[2] = 1
        if request_json["alert"] == '4hr' and webhook[3] == 0:
            X = array(request_json, X)
            webhook[3] = 1
        if request_json["alert"] == '1d' and webhook[4] == 0:
            X = array(request_json, X)
            webhook[4] = 1
        if webhook[0] == 1 and webhook[1] == 1 and webhook[2] == 1 and webhook[3] == 1 and webhook[4] == 1:
            webhook = [0, 0, 0, 0, 0]
            trade(X)
        pickle_out5 = open('webhook.pickle', 'wb')
        pickle.dump(webhook, pickle_out5)
        pickle_out5.close()
        pickle_out6 = open('X.pickle', 'wb')
        pickle.dump(X, pickle_out6)
        pickle_out6.close()
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
