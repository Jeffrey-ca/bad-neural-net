from neural_net import *


# this trains neural net
start = timer()
for b in range(1):
    for i in range(len(inp.keys())):
        train(1)
        a = nn()
        print(a)
for i in range(len(inp.keys())):
    print(i, output(inp[i]))
    print(i, out[i])
end = timer()
print(end-start)
# 0.044341453055449905 --> 0.043935007658902896 ended at 38 with 50 neurons 20 minutes

# reset information
'''X = np.zeros(shape=40)
webhook = [0, 0, 0, 0, 0]
pickle_out5 = open('webhook.pickle', 'wb')
pickle.dump(webhook, pickle_out5)
pickle_out5.close()
pickle_out6 = open('X.pickle', 'wb')
pickle.dump(X, pickle_out6)
pickle_out6.close()
inp = {}
out = {}
pickle_out = open('inputs.pickle', 'wb')
pickle.dump(inp, pickle_out)
pickle_out.close()
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()'''


# reset neural net weights and biases
'''w1 = np.zeros(shape=(100, 40))
b1 = np.zeros(shape=(100))
w2 = np.zeros(shape=(100, 100))
b2 = np.zeros(shape=(100))
w3 = np.zeros(shape=(100, 1))
b3 = np.zeros(shape=(1))
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
'''
'''def nn(in_len):
    loss = 0
    for i in range(in_len):
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




PO_b3 = open("loss.pickle", "wb")
pickle.dump(loss, PO_b3)
PO_b3.close()


PI_w1 = open('loss.pickle', 'rb')
loss = pickle.load(PI_w1)'''


'''def nn():
    loss = 0
    for i in range(len(inp.keys())):
        a = len(inp.keys())
        X = inp[i]
        to = out[i]
        loss += nn(X, to)
    return loss

@jit(nopython=True, parallel=True)
def loss_math(X, to):
    o1 = np.add(np.dot(w1, X), b1)
    activation3(o1)
    o2 = np.add(np.dot(w2, o1), b2)
    activation2(o2)
    o3 = np.add(np.dot(o2, w3), b3)
    loss_array = abs(np.subtract(o3, to))
    loss_2x = np.square(loss_array)
    for p in range(len(loss_2x)):
        loss = loss + loss_2x[p]
    return np.sum(loss)

'''
'''def nn():
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
    return np.sum(loss)'''


