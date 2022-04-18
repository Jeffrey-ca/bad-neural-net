import numpy as np
from numba import jit, cuda
import random
import pickle
from timeit import default_timer as timer
from save_inputs_outputs import save_input


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


def array(num):
    w1 = np.zeros(shape=(num, num))
    b1 = np.zeros(shape=(num))
    w2 = np.zeros(shape=(num, num))
    b2 = np.zeros(shape=(num))
    w3 = np.zeros(shape=(num, 2))
    b3 = np.zeros(shape=(2))


@jit(nopython=True, cache=True, fastmath=True)
def activation(output, num):
    for n in range(0, 25):
        if output[n] > num:
            output[n] = 1
        else:
            output[n] = 0


def nn(data, to):
    o1 = np.add(np.dot(w1, data), b1)
    activation(o1, .5)
    o2 = np.add(np.dot(w2, o1), b2)
    o3 = np.add(np.dot(o2, w3), b3)
    loss_array = np.subtract(o3, to)
    loss_2x = np.square(loss_array)
    loss = 0
    for p in range(len(loss_2x)):
        loss = loss + loss_2x[p]
    return np.sum(loss)


@jit(nopython=True, parallel=True, cache=True, fastmath=True)
def output(data1):
    o1 = np.add(np.dot(w1, data1), b1)
    activation(o1, .5)
    o2 = np.add(np.dot(w2, o1), b2)
    o3 = np.add(np.dot(o2, w3), b3)
    return o3


def train(num1, X, to):
    for z in range(0, num1, 1):
        for a in range(1, 2, 1):
            for c in range(0, 25):
                for b in range(0, 25):
                    hold_loss_w1 = nn(X, to)
                    hold_w1 = w1[c][b]
                    w1[c][b] = random.uniform(-1.0, 1)
                    loss_test_w1 = nn(X, to)
                    if abs(hold_loss_w1) < abs(loss_test_w1):
                        w1[c][b] = hold_w1
            for d in range(0, 25):
                hold_loss_b1 = nn(X, to)
                hold_b1 = b1[d]
                b1[d] = random.uniform(-1.0, 1.0)
                loss_test_b1 = nn(X, to)
                if abs(hold_loss_b1) < abs(loss_test_b1):
                    b1[d] = hold_b1
            for e in range(0, 25):
                for f in range(0, 25):
                    hold_loss_w2 = nn(X, to)
                    hold_w2 = w2[e][f]
                    w2[e][f] = random.uniform(-1.0, 1)
                    loss_test_w2 = nn(X, to)
                    if abs(hold_loss_w2) < abs(loss_test_w2):
                        w2[e][f] = hold_w2
            for g in range(0, 25):
                hold_loss_b2 = nn(X, to)
                hold_b2 = b2[g]
                b2[g] = random.uniform(-1.0, 1.0)
                loss_test_b2 = nn(X, to)
                if abs(hold_loss_b2) < abs(loss_test_b2):
                    b2[g] = hold_b2
            for h in range(0, 25, 1):
                for i in range(0, 2, 1):
                    hold_loss_w3 = nn(X, to)
                    hold_w3 = w3[h][i]
                    w3[h][i] = random.uniform(-1.0, 1)
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


def save():
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


'''rand_nums = np.zeros(shape=(25))
X = np.array(rand_nums)
start = timer()
to = [1.0, .2]
train(100, X, to)
save()
end = timer()
print(output(X))
print(nn(X, to))
print((end-start), 'seconds')'''
