import pickle
import random

import numpy as np

# when the quotes are removed this opens the saved weights and biases
'''PI_w1 = open('w1.pickle', 'rb')
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
b3 = pickle.load(PI_b3)'''

# X is input

X = [69, .42, .23, .1, .83, .53, .79, .23, .98, .77]

# quote from here to the end of line 58 to allow saved weights and biases to be opened and used

w1 = [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]

b1 = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]

w2 = [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]

b2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

w3 = [[1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0],
      [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]]

b3 = [0, 0, 0, 0]


# This calculates the output and loss. The target loss is located here
def nn(data):
    o1 = np.add(np.dot(data, w1), b1)
    o2 = np.add(np.dot(o1, w2), b2)
    o3 = np.add(np.dot(w3, o2), b3)
    target_output = [.69, .420, .69, 1]
    loss_array = np.subtract(o3, target_output)
    loss_2x = np.square(loss_array)
    loss = 0
    for p in range(len(loss_2x)):
        loss = loss + loss_2x[p]
    return loss / 10


# this calculates the output
def output(data1):
    o1 = np.add(np.dot(data1, w1), b1)
    o2 = np.add(np.dot(o1, w2), b2)
    o3 = np.add(np.dot(w3, o2), b3)
    return o3


total_loss = 0
# Train weights and biases
for z in range(1, 100, 1):
    for a in range(1, 5, 1):
        print(nn(X))
        total_loss = total_loss + (nn(X))
        for c in range(0, 10):
            for b in range(0, 10):
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
        for d in range(0, 10):
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
        for e in range(0, 10):
            for f in range(0, 10):
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
        for g in range(0, 10):
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
        for h in range(0, 4):
            for i in range(0, 10):
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
        for j in range(0, 4):
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

print(nn(X))
print('Total Loss:', total_loss)
print(output(X))
print('W1:', w1)
print('B1:', b1)
print('W2:', w2)
print('B2:', b2)
print('W2:', w3)
print('B3:', b3)
