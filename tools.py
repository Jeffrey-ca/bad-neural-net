from neural_net import *

# this trains neural net
'''start = timer()
for b in range(1):
    for i in range(len(out.keys())):
        train(1, inp[i], out[i])
        a = nn(inp[i], out[i])
        print(a)
for i in range(len(out.keys())):
    print(i, output(inp[i]))
    print(out[i])
end = timer()
print(end-start)'''


# edit outputs and inputs
'''pickle_in = open('inputs.pickle', 'rb')
inp = pickle.load(pickle_in)
pickle_in2 = open('outputs.pickle', 'rb')
out = pickle.load(pickle_in2)'''
'''out[20] = np.array([0.5, 0])
out[21] = np.array([0.5, 0])
out[22] = np.array([-.2, 1])
out[23] = np.array([1, -.2])
out[24] = np.array([.6, -.3])
out[25] = np.array([0, 0])
out[26] = np.array([-0.5, .6])
out[27] = np.array([-1, 1])
out[28] = np.array([1, -1])
out[29] = np.array([-1, 1])
out[30] = np.array([-1, 1])'''


'''print(out)
pickle_out = open('inputs.pickle', 'wb')
pickle.dump(inp, pickle_out)
pickle_out.close()
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()'''

# io_pop() to remove item from list
# removes duplication entries in the inp and out dictionaries

'''remove_dup()'''

# this sets default values for trade and position
'''pickle_in3 = open('trade.pickle', 'rb')
trade = pickle.load(pickle_in3)
pickle_in4 = open('pos.pickle', 'rb')
pos = pickle.load(pickle_in4)'''
'''trade = 0
pos = 0
pickle_out4 = open('pos.pickle', 'wb')
pickle.dump(pos, pickle_out4)
pickle_out4.close()
pickle_out3 = open('trade.pickle', 'wb')
pickle.dump(trade, pickle_out3)
pickle_out3.close()'''


# This sets input and output dictionaries to nothing
'''inp = {}
out = {}
pickle_out = open('inputs.pickle', 'wb')
pickle.dump(inp, pickle_out)
pickle_out.close()
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()'''

# change held price for stop loss & take profit
'''heldprice = holdprice(30900, 500)
pickle_out2 = open('heldprice.pickle', 'wb')
pickle.dump(heldprice, pickle_out2)
pickle_out2.close()'''
'''pickle_in2 = open('heldprice.pickle', 'rb')
heldprice = pickle.load(pickle_in2)
print(heldprice)'''

# sets neural net input and webhook counter to zero
'''X = np.zeros(shape=40)
webhook = [0, 0, 0, 0, 0]
pickle_out5 = open('webhook.pickle', 'wb')
pickle.dump(webhook, pickle_out5)
pickle_out5.close()
pickle_out6 = open('X.pickle', 'wb')
pickle.dump(X, pickle_out6)
pickle_out6.close()'''

# this code is the magic code to access last trade profit and loss
'''last_trade = last_trade()
print(last_trade["result"]["data"][0]["closed_pnl"])
last_trade["result"]["data"][0]["closed_pnl"]'''