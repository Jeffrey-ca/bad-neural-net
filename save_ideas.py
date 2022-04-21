import numpy as np
from test import *


def save_input():
    file = open("saved_inputs.txt", "a")
    content = str(X)
    content1 = str(to)
    file.write(content)
    file.write(content1)
    file.close()
    file = open("saved_inputs.txt", "r")
    a = file.read()
    d = a.replace('[', ' ')
    e = d.replace(']', ' ')
    f = e.replace(',', ' ')
    b = f.split()
    for i in range(0, len(b), 27):
        c = [float(b[i]), float(b[i + 1]), float(b[i + 2]), float(b[i + 3]), float(b[i + 4]), float(b[i + 5]), float(b[i + 6]), float(b[i + 7]), float(b[i + 8]), float(b[i + 9]), float(b[i + 10]), float(b[i + 11]), float(b[i + 12]),
             float(b[i + 13]), float(b[i + 14]), float(b[i + 15]), float(b[i + 16]), float(b[i + 17]), float(b[i + 18]), float(b[i + 19]), float(b[i + 20]), float(b[i + 21]), float(b[i + 22]), float(b[i + 23]), float(b[i + 24])]
        m = [float(b[i + 25]), float(b[i + 26])]


'''pickle_in = open('inputs.pickle', 'rb')
inp = pickle.load(pickle_in)'''
inp = {}


def save2(array2):
    inp[len(inp.keys())] = array2
    pickle_out = open('inputs.pickle', 'wb')
    pickle.dump(inp, pickle_out)
    pickle_out.close()

out = {}


def save2(array1):
    out[len(out.keys())] = array1
    pickle_out = open('outputs.pickle', 'wb')
    pickle.dump(out, pickle_out)
    pickle_out.close()




