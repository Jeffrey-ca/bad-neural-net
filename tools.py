from neural_net import *
from trading_def import *
# this trains neural net
'''start = timer()
for b in range(1):
    for i in range(len(inp.keys())):
        train(1, inp[i], out[i])
        save_weights()
        print(nn(inp[i], out[i]))
for i in range(len(inp.keys())):
    print(i, output(inp[i]))
    print(i, out[i])
end = timer()
print(end-start)'''


# 0.044341453055449905 --> 0.043935007658902896 ended at 38 with 50 neurons 20 minutes

# reset information
'''X = np.zeros(shape=40)
web_data = [0, 0, 0, 0, 0]
pickle_out5 = open('webhook.pickle', 'wb')
pickle.dump(web_data, pickle_out5)
pickle_out5.close()
pickle_out6 = open('X.pickle', 'wb')
pickle.dump(X, pickle_out6)
pickle_out6.close()
print(X)
print(web_data)

print(loss_function())'''
'''
inp = {}
out = {}
pickle_out = open('inputs.pickle', 'wb')
pickle.dump(inp, pickle_out)
pickle_out.close()
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()
print(inp)'''
# reset neural net weights and biases
'''w1 = np.zeros(shape=(100, 40))
for a in range(len(w1)):
    for b in range(len(w1[a])):
        w1[a][b] = random.uniform(-1.0, 1.0)
b1 = np.zeros(shape=(100))
for i in range(len(b1)):
    b1[i] = random.uniform(-1.0, 1.0)
w2 = np.zeros(shape=(75, 100))
for a in range(len(w2)):
    for b in range(len(w2[a])):
        w2[a][b] = random.uniform(-1.0, 1.0)
b2 = np.zeros(shape=(75))
for i in range(len(b2)):
    b2[i] = random.uniform(-1.0, 1.0)
w3 = np.zeros(shape=(50,75))
for a in range(len(w3)):
    for b in range(len(w3[a])):
        w3[a][b] = random.uniform(-1.0, 1.0)
b3 = np.zeros(shape=(50))
for i in range(len(b3)):
    b3[i] = random.uniform(-1.0, 1.0)
w4 = np.zeros(shape=(1, 50))
for a in range(len(w4)):
    for b in range(len(w4[a])):
        w4[a][b] = random.uniform(-1.0, 1.0)
b4 = np.zeros(shape=(1))
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
PO_b4.close()'''

times_trained = 0
start = timer()
while loss_function() > .9:
    train(1)
    times_trained += 1
print(loss_function())
print(times_trained)
end = timer()
print(end-start)
'''
print(loss_function())
print(len(out.keys()))
'''

