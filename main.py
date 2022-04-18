from neural_net import *

# todo make data variable based on webhooks

rand_nums = np.zeros(shape=(25))
X = np.array(rand_nums)
start = timer()
to = [1, .1]
train(100, X, to)
save()
end = timer()
print(output(X))
print(nn(X, to))
print((end-start), 'seconds')
