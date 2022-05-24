from flask import Flask, request, abort
from trading_def import *
from neural_net import *
from flask_ngrok import run_with_ngrok
import time


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
            print('1m')
        if request_json["alert"] == '12m' and webhook[1] == 0:
            X = array(request_json, X)
            webhook[1] = 1
            print('12m')
        if request_json["alert"] == '1hr' and webhook[2] == 0:
            X = array(request_json, X)
            webhook[2] = 1
            print('1hr')
        if request_json["alert"] == '4hr' and webhook[3] == 0:
            X = array(request_json, X)
            webhook[3] = 1
            print('4hr')
        if request_json["alert"] == '1d' and webhook[4] == 0:
            X = array(request_json, X)
            webhook[4] = 1
            print('1d')
        if webhook[0] == 1 and webhook[1] == 1 and webhook[2] == 1 and webhook[3] == 1 and webhook[4] == 1:
            webhook[0] = 0
            webhook[1] = 0
            webhook[2] = 0
            webhook[3] == 0
            webhook[4] == 0
            amount = 75
            price = X[7]
            outpu = output(X)
            positioninfo = position_info()
            if str(positioninfo) == 'None':
                position = str(None)
            else:
                position = positioninfo["result"]["side"]
            if str(position) == 'None':
                if outpu[0] >= .5:
                    long_(amount, price)
                    save_in_out(X)
                elif outpu[0] <= -.5:
                    short(amount, price)
                    save_in_out(X)
            elif position == 'Buy':
                if outpu[0] <= -.05:
                    short(amount * 2, price)
                    time.sleep(1)
                    auto_label_last()
                    time.sleep(1)
                    save_in_out(X)
                elif outpu[0] < .5 and outpu[0] > -.5:
                    short(amount, price)
                    time.sleep(1)
                    auto_label_last()
            elif position == 'Sell':
                if outpu[0] >= .05:
                    long_(amount * 2, price)
                    time.sleep(1)
                    auto_label_last()
                    time.sleep(1)
                    save_in_out(X)
                elif outpu[0] < .5 and outpu[0] > -.5:
                    long_(amount, price)
                    time.sleep(1)
                    auto_label_last()
        pickle_out5 = open('webhook.pickle', 'wb')
        pickle.dump(webhook, pickle_out5)
        pickle_out5.close()
        pickle_out6 = open('X.pickle', 'wb')
        pickle.dump(X, pickle_out6)
        pickle_out6.close()
        pickle_out2 = open('outputs.pickle', 'wb')
        pickle.dump(out, pickle_out2)
        pickle_out2.close()
        pickle_out = open('inputs.pickle', 'wb')
        pickle.dump(inp, pickle_out)
        pickle_out.close()
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
