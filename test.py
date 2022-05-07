from neural_net import *

'''start = timer()
for b in range(5):
    for i in range(len(out.keys())):
        train(1)
print('0', output(inp[0]))
print(out[0])
end = timer()
print(end-start)'''


pickle_in = open('wh.pickle', 'rb')
wh = pickle.load(pickle_in)
X = array(wh)
out = output(X)
save_in_out(X, output(X))

# {'EMA 21': '38500.21186664863', 'Yellow Diamond': '0', 'Trend Change': '0', 'Green Dot': '0', 'Red X': '0', 'Manipulation': '0', 'Red Diamond': '0', 'Blood Diamond': '0', 'Close': '39062.5', 'Open': '38947', 'High': '39077.5', 'Low': '38946.5', 'Volume': '23983115'}
