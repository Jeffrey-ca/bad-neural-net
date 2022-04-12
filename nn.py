import pickle
import random
import numpy as np

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

# X is input
# todo make input variable
''''''
X = [.69, .42, .23, .1, .83, .53, .79, .23, .98, .77, .69, .42, .23, .1, .83, .53, .79, .23, .98, .77, .69, .42, .23, .1, .83, .53, .79, .23, .98, .77, .69, .42, .23, .1, .83, .53, .79, .23, .98, .77, .69, .42, .23, .1, .83, .53, .79, .23, .98, .77,
     .69, .42, .23, .1, .83, .53, .79, .23, .98, .77, .69, .42, .23, .1, .83, .53, .79, .23, .98, .77, .69, .42, .23, .1, .83, .53, .79, .23, .98, .77, .69, .42, .23, .1, .83, .53, .79, .23, .98, .77, .69, .42, .23, .1, .83, .53, .79, .23, .98, .77, ]


# TODO make variable target outout

# activation

def activation(output, num):
    for n in range(0, 100):
        if output[n] > num:
            output[n] = 1
        else:
            output[n] = 0

# This calculates the output and loss. The target loss is located here


def nn(data):
    o1 = np.add(np.dot(w1, data), b1)
    o2 = np.add(np.dot(w2, o1), b2)
    activation(o2, .3)
    o3 = np.add(np.dot(w3, o2), b3)
    target_output = [1, .1]
    loss_array = np.subtract(o3, target_output)
    loss_2x = np.square(loss_array)
    loss = 0
    for p in range(len(loss_2x)):
        loss = loss + loss_2x[p]
    return loss


# this calculates the output
def output(data1):
    o1 = np.add(np.dot(w1, data1), b1)
    o2 = np.add(np.dot(w2, o1), b2)
    activation(o2, .3)
    o3 = np.add(np.dot(w3, o2), b3)
    return o3


# trains everything
def train(num1, num2):
    total_loss = 0
    for z in range(1, num1, 1):
        for a in range(1, num2, 1):
            total_loss = total_loss + (nn(X))
            for c in range(0, 100):
                for b in range(0, 100):
                    hold_loss_w1 = nn(X)
                    hold_w1 = w1[c][b]
                    w1[c][b] = random.uniform(-1.0, 1)
                    loss_test_w1 = nn(X)
                    if abs(hold_loss_w1) < abs(loss_test_w1):
                        w1[c][b] = hold_w1
                    elif abs(loss_test_w1) < abs(hold_loss_w1):
                        PO_w1 = open("w1.pickle", "wb")
                        pickle.dump(w1, PO_w1)
                        PO_w1.close()
            for d in range(0, 100):
                hold_loss_b1 = nn(X)
                hold_b1 = b1[d]
                b1[d] = random.uniform(-1.0, 1.0)
                loss_test_b1 = nn(X)
                if abs(hold_loss_b1) < abs(loss_test_b1):
                    b1[d] = hold_b1
                elif abs(loss_test_b1) < abs(hold_loss_b1):
                    PO_b1 = open("b1.pickle", "wb")
                    pickle.dump(b1, PO_b1)
                    PO_b1.close()
            for e in range(0, 100):
                for f in range(0, 100):
                    hold_loss_w2 = nn(X)
                    hold_w2 = w2[e][f]
                    w2[e][f] = random.uniform(-1.0, 1)
                    loss_test_w2 = nn(X)
                    if abs(hold_loss_w2) < abs(loss_test_w2):
                        w2[e][f] = hold_w2
                    elif abs(loss_test_w2) < abs(hold_loss_w2):
                        PO_w2 = open("w2.pickle", "wb")
                        pickle.dump(w2, PO_w2)
                        PO_w2.close()
            for g in range(0, 100):
                hold_loss_b2 = nn(X)
                hold_b2 = b2[g]
                b2[g] = random.uniform(-1.0, 1.0)
                loss_test_b2 = nn(X)
                if abs(hold_loss_b2) < abs(loss_test_b2):
                    b2[g] = hold_b2
                elif abs(loss_test_b2) < abs(hold_loss_b2):
                    PO_b2 = open("b2.pickle", "wb")
                    pickle.dump(b2, PO_b2)
                    PO_b2.close()
            for h in range(0, 2, 1):
                for i in range(0, 100, 1):
                    hold_loss_w3 = nn(X)
                    hold_w3 = w3[h][i]
                    w3[h][i] = random.uniform(-1.0, 1)
                    loss_test_w3 = nn(X)
                    if abs(hold_loss_w3) < abs(loss_test_w3):
                        w3[h][i] = hold_w3
                    elif abs(loss_test_w3) < abs(hold_loss_w3):
                        PO_w3 = open("w3.pickle", "wb")
                        pickle.dump(w3, PO_w3)
                        PO_w3.close()
            for j in range(0, 2):
                hold_loss_b3 = nn(X)
                hold_b3 = b3[j]
                b3[j] = random.uniform(-1.0, 1.0)
                loss_test_b3 = nn(X)
                if abs(hold_loss_b3) < abs(loss_test_b3):
                    b3[j] = hold_b3
                elif abs(loss_test_b3) < abs(hold_loss_b3):
                    PO_b3 = open("b3.pickle", "wb")
                    pickle.dump(b3, PO_b3)
                    PO_b3.close()
