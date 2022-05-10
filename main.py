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
        X = array(request.json)
        out = output(X)
        save_in_out(X, output(X))
        print(X)
        print(output(X))
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
