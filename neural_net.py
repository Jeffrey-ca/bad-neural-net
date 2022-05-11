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
#TODO change array size for multiple webhooks
'''w1 = np.zeros(shape=(50, 12))
b1 = np.zeros(shape=(50))
w2 = np.zeros(shape=(50, 50))
b2 = np.zeros(shape=(50))
w3 = np.zeros(shape=(50, 2))
b3 = np.zeros(shape=(2))'''


def activation2(output):
    for n in range(0, 50):
        output[n] = 1/(1+(math.e**-(output[n])))


def activation3(output):
    for n in range(0, 50):
        output[n] = (2/(1+(math.e**-(2*output[n]))))-1

#TODO make this parallel 
def nn(X, to):
    loss = 0
    for i in range(len(inp.keys())):
        o1 = np.add(np.dot(w1, inp[i]), b1)
        activation3(o1)
        o2 = np.add(np.dot(w2, o1), b2)
        activation2(o2)
        o3 = np.add(np.dot(o2, w3), b3)
        loss_array = np.subtract(o3, out[i])
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
                    for b in range(0, 10):
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


pickle_in = open('inputs.pickle', 'rb')
inp = pickle.load(pickle_in)
pickle_in2 = open('outputs.pickle', 'rb')
out = pickle.load(pickle_in2)


def save_in_out(array2, array1):
    inp[len(inp.keys())] = array2
    pickle_out = open('inputs.pickle', 'wb')
    pickle.dump(inp, pickle_out)
    pickle_out.close()
    out[len(out.keys())] = array1
    pickle_out2 = open('outputs.pickle', 'wb')
    pickle.dump(out, pickle_out2)
    pickle_out2.close()

#TODO make this differentiate between each array
def array(request_json):
    X = np.zeros(shape=12)
    X[0] = float(request_json["0"]) / 10
    X[1] = float(request_json["1"]) / 10
    X[2] = float(request_json["2"])
    X[3] = float(request_json["3"]) / 100
    if request_json["4"] == 'null':
        X[4] = 0
    else:
        X[4] = float(request_json["4"])
    if request_json["5"] == 'null':
        X[5] = 0
    else:
        X[5] = float(request_json["5"])
    if request_json["6"] == 'null':
        X[6] = 0
    else:
        X[6] = float(request_json["6"])
    X[7] = float(request_json["7"]) / 100000
    X[8] = float(request_json["8"]) / 100000
    X[9] = float(request_json["9"]) / 100000
    X[10] = float(request_json["10"]) / 100000
    X[11] = float(request_json["11"]) / 100000000
    if X[4] == 'null':
        X[4] = 0
    if X[5] == 'null':
        X[5] = 0
    if X[6] == 'null':
        X[6] = 0
    return X

# TODO fix this so it works


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


#TODO add automatic labeling of previous trades for easier training