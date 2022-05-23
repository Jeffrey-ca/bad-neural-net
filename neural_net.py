import numpy as np
from numba import jit, cuda
import math
import random
import pickle
from timeit import default_timer as timer


# Loads weights, biases, and training data

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
PI_w4 = open('w4.pickle', 'rb')
w4 = pickle.load(PI_w4)
PI_b4 = open('b4.pickle', 'rb')
b4 = pickle.load(PI_b4)
pickle_in = open('inputs.pickle', 'rb')
inp = pickle.load(pickle_in)
pickle_in2 = open('outputs.pickle', 'rb')
out = pickle.load(pickle_in2)


# Two activation functions for neural net
def activation2(output):
    for n in range(0, 100):
        output[n] = 1/(1+(math.e**-(output[n])))


def activation3(output):
    for n in range(0, 100):
        output[n] = (2/(1+(math.e**-(2*output[n]))))-1

def activation(output):
    return max(0.0, output)


# TODO make nn function parallel
# Calculates loss of the neural net
def nn(x, to):
    loss = 0
    for i in range(len(inp.keys())):
        o1 = np.add(np.dot(w1, inp[i]), b1)
        activation3(o1)
        o2 = np.add(np.dot(w2, o1), b2)
        activation2(o2)
        o3 = np.add(np.dot(w3, o2), b3)
        activation(o3)
        o4 = np.add(np.dot(w4, o3), b4)
        loss_array = abs(np.subtract(o4, out[i]))
        loss_2x = np.square(loss_array)
        for p in range(len(loss_2x)):
            loss = abs(loss) + abs(loss_2x[p])
    return np.sum(loss)


# Produces the output of neural net
def output(X):
    o1 = np.add(np.dot(w1, X), b1)
    activation3(o1)
    o2 = np.add(np.dot(w2, o1), b2)
    activation2(o2)
    o3 = np.add(np.dot(w3, o2), b3)
    activation(o3)
    o4 = np.add(np.dot(w4, o3), b4)
    return o4


# Train the neural net
def train(num1, X, to):
    for x in range(0, num1, 1):
        for c in range(0, len(w1)):
            for b in range(0, len(w1[0])):
                hold_loss_w1 = nn(X, to)
                hold_w1 = w1[c][b]
                w1[c][b] = random.uniform(-1.0, 1.0)
                loss_test_w1 = nn(X, to)
                if abs(hold_loss_w1) < abs(loss_test_w1):
                    w1[c][b] = hold_w1
        for d in range(0, len(b1)):
            hold_loss_b1 = nn(X, to)
            hold_b1 = b1[d]
            b1[d] = random.uniform(-1.0, 1.0)
            loss_test_b1 = nn(X, to)
            if abs(hold_loss_b1) < abs(loss_test_b1):
                b1[d] = hold_b1
        for e in range(0, len(w2)):
            for f in range(0, len(w2[0])):
                hold_loss_w2 = nn(X, to)
                hold_w2 = w2[e][f]
                w2[e][f] = random.uniform(-1.0, 1.0)
                loss_test_w2 = nn(X, to)
                if abs(hold_loss_w2) < abs(loss_test_w2):
                    w2[e][f] = hold_w2
        for g in range(0, len(b2)):
            hold_loss_b2 = nn(X, to)
            hold_b2 = b2[g]
            b2[g] = random.uniform(-1.0, 1.0)
            loss_test_b2 = nn(X, to)
            if abs(hold_loss_b2) < abs(loss_test_b2):
                b2[g] = hold_b2
        for e in range(0, len(w3)):
            for f in range(0, len(w3[0])):
                hold_loss_w3 = nn(X, to)
                hold_w3 = w3[e][f]
                w3[e][f] = random.uniform(-1.0, 1.0)
                loss_test_w3 = nn(X, to)
                if abs(hold_loss_w3) < abs(loss_test_w3):
                    w3[e][f] = hold_w3
        for g in range(0, len(b3)):
            hold_loss_b3 = nn(X, to)
            hold_b3 = b3[g]
            b3[g] = random.uniform(-1.0, 1.0)
            loss_test_b3 = nn(X, to)
            if abs(hold_loss_b3) < abs(loss_test_b3):
                b3[g] = hold_b3
        for h in range(0, len(w4)):
            for i in range(0, len(w4[0])):
                hold_loss_w4 = nn(X, to)
                hold_w4 = w4[h][i]
                w4[h][i] = random.uniform(-1.0, 1.0)
                loss_test_w4 = nn(X, to)
                if abs(hold_loss_w4) < abs(loss_test_w4):
                    w4[h][i] = hold_w4
        for j in range(0, len(b4)):
            hold_loss_b4 = nn(X, to)
            hold_b4 = b4[j]
            b4[j] = random.uniform(-1.0, 1.0)
            loss_test_b4 = nn(X, to)
            if abs(hold_loss_b4) < abs(loss_test_b4):
                b4[j] = hold_b4
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
    PO_w4 = open("w4.pickle", "wb")
    pickle.dump(w4, PO_w4)
    PO_w4.close()
    PO_b4 = open("b4.pickle", "wb")
    pickle.dump(b4, PO_b4)
    PO_b4.close()
