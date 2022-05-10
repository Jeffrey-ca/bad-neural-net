from neural_net import *

#this trains neural net
start = timer()
for b in range(5):
    for i in range(len(out.keys())):
        train(1, inp[i], out[i])
        a = nn(inp[i], out[i])
        print(a)
        save_weights()
print('0', output(inp[0]))
print(out[0])
'''print('1', output(inp[1]))
print(out[1])'''
end = timer()
print(end-start)

## edit outputs and inputs
'''pickle_in = open('inputs.pickle', 'rb')
inp = pickle.load(pickle_in)
pickle_in2 = open('outputs.pickle', 'rb')
out = pickle.load(pickle_in2)
out[0] = np.array([-1.0, 1.0])
print(out)
pickle_out = open('inputs.pickle', 'wb')
pickle.dump(inp, pickle_out)
pickle_out.close()
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()'''

# {'EMA 21': '38500.21186664863', 'Yellow Diamond': '0', 'Trend Change': '0', 'Green Dot': '0', 'Red X': '0', 'Manipulation': '0', 'Red Diamond': '0', 'Blood Diamond': '0', 'Close': '39062.5', 'Open': '38947', 'High': '39077.5', 'Low': '38946.5', 'Volume': '23983115'}
