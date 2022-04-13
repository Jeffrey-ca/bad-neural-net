from neural_net import *

# todo make data variable based on webhooks

rand_nums = np.random.uniform(-1.0, 1, 25)
X = np.array(rand_nums)
start = timer()
train(100, X)
end = timer()
print(output(X))
print(nn(X))
print((end-start), 'seconds')

