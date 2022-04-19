from flask import Flask, request, abort
from trade_options import *
from neural_net import *

app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    if request.method == 'POST':
        print(request.json)
        # TODO add way to read json file and turn data into array
        rand_nums = np.zeros(shape=(25))
        X = np.array(rand_nums)  # array from request
        nn_output = nn(X)
        if nn_output[0] >= .8:
            long()
        elif nn_output[1] >= .8:
            short()
        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    app.run()
