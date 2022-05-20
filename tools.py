from neural_net import *


# this trains neural net
start = timer()
for b in range(26):
    for i in range(len(inp.keys())):
        train(1, inp[i], out[i])
        a = nn(inp[i], out[i])
        print(a)
for i in range(len(inp.keys())):
    print(i, output(inp[i]))
    print(i, out[i])
end = timer()
print(end-start)
# 0.044341453055449905 --> 0.043935007658902896 ended at 38


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