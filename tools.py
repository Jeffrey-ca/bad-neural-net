from turtle import pos
from neural_net import *


# this trains neural net
'''start = timer()
for b in range(2):
    for i in range(len(out.keys())):
        train(1, inp[i], out[i])
        a = nn(inp[i], out[i])
        print(a)
for i in range(len(out.keys())):
    print(i, output(inp[i]))
    print(out[i])
end = timer()
print(end-start)'''

# change held price for stop loss & take profit
'''heldprice = holdprice(30400, 1000)
pickle_out2 = open('heldprice.pickle', 'wb')
pickle.dump(heldprice, pickle_out2)
pickle_out2.close()
'''
'''io_pop(1)
pickle_out = open('inputs.pickle', 'wb')
pickle.dump(inp, pickle_out)
pickle_out.close()
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()
print(out)'''
'''pickle_in3 = open('trade.pickle', 'rb')
trade = pickle.load(pickle_in3)
pickle_in4 = open('pos.pickle', 'rb')
pos = pickle.load(pickle_in4)
pickle_in2 = open('heldprice.pickle', 'rb')
heldprice = pickle.load(pickle_in2)
print(trade)'''
print(out)