
from neural_net import *

# todo make data variable based on webhooks

# generates random numbers for input with set target output
rand_nums = np.random.uniform(-1, 1, size=(10))
'''to = [1, .1]
X = np.array(rand_nums)'''
# This code trains neural net on previous runs

start = timer()
for b in range(500):
    for i in range(len(out.keys())):
        train(1, inp[i], out[i])
        save_weights()
end = timer()
print((end-start), 'seconds')
print('0', output(inp[0]))
print(out[0])
print('1', output(inp[1]))
print(out[1])
# this code is used to save inputs and outputs
'''save_in_out(X, output(X))'''

# this code is used to label the data for training
'''out[1] = np.array([0.8, -0.8])
print(out)
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()
'''