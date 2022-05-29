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


def activation2(output):
    for n in range(0, len(output)):
        output[n] = 1/(1+(math.e**-(output[n])))
    return output


def activation3(output):
    for n in range(0, len(output)):
        output[n] = (2/(1+(math.e**-(2*output[n]))))-1
    return output


def activation(output):
    for i in range(len(output)):
        output[i] = output[i]/abs(np.sum(output))
    return output


# TODO make nn function parallel
def loss_function():
    loss = 0
    for i in range(0, len(inp.keys())):
        o4 = output(inp[i])
        loss_array = abs(np.subtract(o4, out[i]))
        loss_2x = np.square(loss_array)
        for p in range(len(loss_2x)):
            loss = abs(loss) + abs(loss_2x[p])
    return np.sum(loss)


def output(X):
    o1 = np.add(np.dot(w1, X), b1)
    o1 = activation(o1)
    o2 = np.add(np.dot(w2, o1), b2)
    o2 = activation3(o2)
    o3 = np.add(np.dot(w3, o2), b3)
    o3 = activation2(o3)
    o4 = np.add(np.dot(w4, o3), b4)
    return o4


def train(num_train):
    for i in range(num_train):
        train_function(w1, b1)
        train_function(w2, b2)
        train_function(w3, b3)
        train_function(w4, b4)


def train_function(weight, bias):
    for i in range(0, len(weight)):
        for b in range(0, len(weight[0])):
            hold_loss = loss_function()
            hold_weight = weight[i][b]
            weight[i][b] = random.uniform(-1.0, 1.0)
            loss_test = loss_function()
            if abs(hold_loss) < abs(loss_test):
                weight[i][b] = hold_weight
            else:
                print(loss_test)
        save_weights_biases()
        for d in range(0, len(bias)):
            hold_loss_bias = loss_function()
            hold_bias = bias[d]
            bias[d] = random.uniform(-1.0, 1.0)
            loss_test_bias = loss_function()
            if abs(hold_loss_bias) < abs(loss_test_bias):
                bias[d] = hold_bias
            else:
                print(loss_test_bias)
        save_weights_biases()


def save_weights_biases():
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

