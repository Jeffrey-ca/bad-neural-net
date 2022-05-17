import numpy as np
from numba import jit, cuda
import math
import random
import pickle
from timeit import default_timer as timer


# Change later to be input

PI_w1 = open('w1.pickle', 'rb')
w1 = pickle.load(PI_w1)
PI_b1 = open('b1.pickle', 'rb')
b1 = pickle.load(PI_b1)
PI_w2 = open('w2.pickle', 'rb')
w2 = pickle.load(PI_w2)
PI_b2 = open('b2.pickle', 'rb')
b2 = pickle.load(PI_b2)
PI_w3 = open('w3.pickle', 'rb')
w3 = pickle.load(PI_w3)
PI_b3 = open('b3.pickle', 'rb')
b3 = pickle.load(PI_b3)

# use to change size of neural net before training
'''w1 = np.zeros(shape=(50, 40))
b1 = np.zeros(shape=(50))
w2 = np.zeros(shape=(50, 50))
b2 = np.zeros(shape=(50))
w3 = np.zeros(shape=(50, 2))
b3 = np.zeros(shape=(2))'''

PO_w1 = open("w1.pickle", "wb")
pickle.dump(w1, PO_w1)
PO_w1.close()
PO_b1 = open("b1.pickle", "wb")
pickle.dump(b1, PO_b1)
PO_b1.close()
PO_w2 = open("w2.pickle", "wb")
pickle.dump(w2, PO_w2)
PO_w2.close()
PO_b2 = open("b2.pickle", "wb")
pickle.dump(b2, PO_b2)
PO_b2.close()
PO_w3 = open("w3.pickle", "wb")
pickle.dump(w3, PO_w3)
PO_w3.close()
PO_b3 = open("b3.pickle", "wb")
pickle.dump(b3, PO_b3)
PO_b3.close()
pickle_in = open('inputs.pickle', 'rb')
inp = pickle.load(pickle_in)
pickle_in2 = open('outputs.pickle', 'rb')
out = pickle.load(pickle_in2)


def activation2(output):
    for n in range(0, 50):
        output[n] = 1/(1+(math.e**-(output[n])))


def activation3(output):
    for n in range(0, 50):
        output[n] = (2/(1+(math.e**-(2*output[n]))))-1

# TODO make nn function parallel


def nn(X, to):
    loss = 0
    for i in range(len(inp.keys())):
        o1 = np.add(np.dot(w1, inp[i]), b1)
        activation3(o1)
        o2 = np.add(np.dot(w2, o1), b2)
        activation2(o2)
        o3 = np.add(np.dot(o2, w3), b3)
        loss_array = abs(np.subtract(o3, out[i]))
        loss_2x = np.square(loss_array)
        for p in range(len(loss_2x)):
            loss = loss + loss_2x[p]
    return np.sum(loss)


def output(data1):
    o1 = np.add(np.dot(w1, data1), b1)
    activation3(o1)
    o2 = np.add(np.dot(w2, o1), b2)
    activation2(o2)
    o3 = np.add(np.dot(o2, w3), b3)
    return o3


def train(num1, X, to):
    for x in range(0, num1, 1):
        for z in range(0, 1, 1):
            for a in range(1, 2, 1):
                for c in range(0, 50):
                    for b in range(0, 40):
                        hold_loss_w1 = nn(X, to)
                        hold_w1 = w1[c][b]
                        w1[c][b] = random.uniform(-1.0, 1.0)
                        loss_test_w1 = nn(X, to)
                        if abs(hold_loss_w1) < abs(loss_test_w1):
                            w1[c][b] = hold_w1
                for d in range(0, 50):
                    hold_loss_b1 = nn(X, to)
                    hold_b1 = b1[d]
                    b1[d] = random.uniform(-1.0, 1.0)
                    loss_test_b1 = nn(X, to)
                    if abs(hold_loss_b1) < abs(loss_test_b1):
                        b1[d] = hold_b1
                for e in range(0, 50):
                    for f in range(0, 50):
                        hold_loss_w2 = nn(X, to)
                        hold_w2 = w2[e][f]
                        w2[e][f] = random.uniform(-1.0, 1.0)
                        loss_test_w2 = nn(X, to)
                        if abs(hold_loss_w2) < abs(loss_test_w2):
                            w2[e][f] = hold_w2
                for g in range(0, 50):
                    hold_loss_b2 = nn(X, to)
                    hold_b2 = b2[g]
                    b2[g] = random.uniform(-1.0, 1.0)
                    loss_test_b2 = nn(X, to)
                    if abs(hold_loss_b2) < abs(loss_test_b2):
                        b2[g] = hold_b2
                for h in range(0, 50, 1):
                    for i in range(0, 2, 1):
                        hold_loss_w3 = nn(X, to)
                        hold_w3 = w3[h][i]
                        w3[h][i] = random.uniform(-1.0, 1.0)
                        loss_test_w3 = nn(X, to)
                        if abs(hold_loss_w3) < abs(loss_test_w3):
                            w3[h][i] = hold_w3
                for j in range(0, 1):
                    hold_loss_b3 = nn(X, to)
                    hold_b3 = b3[j]
                    b3[j] = random.uniform(-1.0, 1.0)
                    loss_test_b3 = nn(X, to)
                    if abs(hold_loss_b3) < abs(loss_test_b3):
                        b3[j] = hold_b3
    save_weights()


def save_weights():
    PO_w1 = open("w1.pickle", "wb")
    pickle.dump(w1, PO_w1)
    PO_w1.close()
    PO_b1 = open("b1.pickle", "wb")
    pickle.dump(b1, PO_b1)
    PO_b1.close()
    PO_w2 = open("w2.pickle", "wb")
    pickle.dump(w2, PO_w2)
    PO_w2.close()
    PO_b2 = open("b2.pickle", "wb")
    pickle.dump(b2, PO_b2)
    PO_b2.close()
    PO_w3 = open("w3.pickle", "wb")
    pickle.dump(w3, PO_w3)
    PO_w3.close()
    PO_b3 = open("b3.pickle", "wb")
    pickle.dump(b3, PO_b3)
    PO_b3.close()


def save_in_out(array2, array1):
    inp[len(inp.keys())] = array2
    pickle_out = open('inputs.pickle', 'wb')
    pickle.dump(inp, pickle_out)
    pickle_out.close()
    out[len(out.keys())] = array1
    pickle_out2 = open('outputs.pickle', 'wb')
    pickle.dump(out, pickle_out2)
    pickle_out2.close()


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

    return X

# TODO fix remove_dup so it works


def remove_dup():
    for i in range(len(inp.keys())):
        for e in range(len(inp.keys())):
            if inp[i].any == inp[e].any:
                inp.pop(e)
                out.pop(e)


def io_pop(num):
    out.pop(num)
    inp.pop(num)


def holdprice(price, sl_tp):
    price1 = price - sl_tp
    price2 = price + sl_tp
    heldprice = [int(price1), int(price2)]
    pickle_out2 = open('heldprice.pickle', 'wb')
    pickle.dump(heldprice, pickle_out2)
    pickle_out2.close()

def reset():
    trade = 0
    pos = 0
    pickle_out4 = open('pos.pickle', 'wb')
    pickle.dump(pos, pickle_out4)
    pickle_out4.close()
    pickle_out3 = open('trade.pickle', 'wb')
    pickle.dump(trade, pickle_out3)
    pickle_out3.close()
    X = np.zeros(shape=40)
    webhook = [0, 0, 0, 0, 0]
    pickle_out5 = open('webhook.pickle', 'wb')
    pickle.dump(webhook, pickle_out5)
    pickle_out5.close()
    pickle_out6 = open('X.pickle', 'wb')
    pickle.dump(X, pickle_out6)
    pickle_out6.close()

def reset_training_data():
    inp = {}
    out = {}
    pickle_out = open('inputs.pickle', 'wb')
    pickle.dump(inp, pickle_out)
    pickle_out.close()
    pickle_out2 = open('outputs.pickle', 'wb')
    pickle.dump(out, pickle_out2)
    pickle_out2.close()

def trade(X): #TODO for save_in_out add logic with magic code to automatically label previous trades as good or bad
    pickle_in3 = open('trade.pickle', 'rb')
    trade = pickle.load(pickle_in3)
    pickle_in4 = open('pos.pickle', 'rb')
    pos = pickle.load(pickle_in4)
    pickle_in2 = open('heldprice.pickle', 'rb')
    heldprice = pickle.load(pickle_in2)
    amount = 30
    variable_sl_tp = 500
    amountx2 = amount * 2
    price = X[7] * 100000
    out = output(X)
    print(output(X))
    if out[0] > 0.5 and out[1] < 0.5 and trade == 0:
        long_(amount, price, variable_sl_tp)
        pos = 1
        trade += 1
        save_in_out(X, output(X))
        holdprice(price, variable_sl_tp)
        print('This should be first trade')
    elif out[1] > 0.5 and out[0] < 0.5 and trade == 0:
        short(amount, price, variable_sl_tp)
        trade -= 1
        pos = -1
        save_in_out(X, output(X))
        holdprice(price, variable_sl_tp)
        print('This should be first trade')
    elif out[0] > 0.5 and out[1] < 0.5 and trade != 0 and pos != 1:
        long_(amountx2, price, variable_sl_tp)
        pos = 1
        save_in_out(X, output(X))
        holdprice(price, variable_sl_tp)
        print('This should be after first trade')
    elif out[1] > 0.5 and out[0] < 0.5 and trade != 0 and pos != -1:
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

# TODO add automatic labeling of previous trades for easier training
