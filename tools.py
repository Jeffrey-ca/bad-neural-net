from neural_net import *
import pickle


# this trains neural net
'''start = timer()
for b in range(4):
    for i in range(len(inp.keys())):
        train(1, inp[i], out[i])
        a = nn(inp[i], out[i])
        print(a)
for i in range(len(out.keys())):
    print(i, output(inp[i]))
    print(i, out[i])
end = timer()
print(end-start)'''

'''pickle_in5 = open('webhook.pickle', 'rb')
webhook = pickle.load(pickle_in5)
pickle_in6 = open('X.pickle', 'rb')
X = pickle.load(pickle_in6)
pickle_in = open('inputs.pickle', 'rb')
inp = pickle.load(pickle_in)
pickle_in2 = open('outputs.pickle', 'rb')
out = pickle.load(pickle_in2)

inp = {}
out = {-1: [0]}
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
print(inp)
print(out)