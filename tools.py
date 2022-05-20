from neural_net import *
import pickle


# this trains neural net
'''start = timer()
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
# 0.044341453055449905 --> 0.043935007658902896 ended at 38'''

'''pickle_in5 = open('webhook.pickle', 'rb')
webhook = pickle.load(pickle_in5)
pickle_in6 = open('X.pickle', 'rb')
X = pickle.load(pickle_in6)
pickle_in = open('inputs.pickle', 'rb')
inp = pickle.load(pickle_in)
pickle_in2 = open('outputs.pickle', 'rb')
out = pickle.load(pickle_in2)

out[10] = [0]
out[14] = [.8]
out[24] = [-.5]
out[25] = [-.8]
out[26] = [-.8]
out[28] = [-.8]
out[29] = [-.8]
out[30] = [-.8]
out[31] = [-.8]
out[32] = [-.8]
out[33] = [-.8]
out[35] = [-.8]
out[36] = [-.8]
out[38] = [-.8]
out.pop(39)
inp.pop(39)
out.pop(40)
inp.pop(40)
out.pop(41)
inp.pop(41)
out.pop(42)
inp.pop(42)

pickle_out = open('inputs.pickle', 'wb')
pickle.dump(inp, pickle_out)
pickle_out.close()
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()
X = np.zeros(shape=40)
webhook = [0, 0, 0, 0, 0, 0]
pickle_out5 = open('webhook.pickle', 'wb')
pickle.dump(webhook, pickle_out5)
pickle_out5.close()
pickle_out6 = open('X.pickle', 'wb')
pickle.dump(X, pickle_out6)
pickle_out6.close()'''

print(out)