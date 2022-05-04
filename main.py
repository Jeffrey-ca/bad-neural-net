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
        request_json = request.json
        wh = open("wh.pickle", "wb")
        pickle.dump(request_json, wh)
        wh.close()
        print(request_json)
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
