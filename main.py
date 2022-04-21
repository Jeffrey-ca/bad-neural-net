from flask import Flask, request, abort
from trade_options import *
from neural_net import *
from pybit import HTTP

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(output(X))
        save_input(X, output(X))
        print(request.json)
        long = 0
        short = 0
        trade = long + short
        if trade == 0:
            # TODO add way to read json file and turn data into array
            rand_nums = np.zeros(shape=(25))
            X = np.array(rand_nums)  # array from request
            nn_output = nn(X)
            if nn_output[0] >= .8 and long != 1:
                long()
                long += 1
            elif nn_output[1] >= .8 and short != 1:
                short() 
                short += 1
        if trade == 1:
            nn_output = nn(X)
            if long == 1 and nn_output[0] < .5:
                close()
                long -= 1
            if short == 1 and nn_output[1] < .5:
                close()
                short -= 1
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
