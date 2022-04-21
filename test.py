from neural_net import *

# todo make data variable based on webhooks

# this code trains the neural net
rand_nums = np.zeros(shape=(25))
X = np.array(rand_nums)
start = timer()
to = [1, .1]
train(10, X, to)
save()
end = timer()
print(output(X))
print(nn(X, to))
print((end-start), 'seconds')

# this code produces output from neural net
print(output(X))
save_input(X, output(X))
'''
file = open("saved_inputs.txt", "r")
output_of_nn = file.read()
print(output_of_nn)
'''
