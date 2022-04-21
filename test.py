from asyncore import read
from neural_net import *

# todo make data variable based on webhooks

# this code trains the neural net
'''rand_nums = np.random.uniform(-1, 1, size=(25))
to = [1, .1]
X = np.array(rand_nums)'''
file = open("saved_inputs.txt", "r")
read_file = file.read()

X = np.asarray(read_file[0:304], dtype=float)
print(X)
to = np.asarray(read_file[304:328], dtype=float)
print(to)
start = timer()
train(10, X, to)
save()
end = timer()
print(output(X))
print(nn(X, to))
print((end-start), 'seconds')

# this code produces output from neural net
'''print(output(X))
save_input(X, output(X))'''
'''
file = open("saved_inputs.txt", "r")
output_of_nn = file.read()
print(output_of_nn)
'''
