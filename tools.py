from neural_net import *

# this trains neural net
'''start = timer()
for b in range(5):
    for i in range(len(out.keys())):
        train(1, inp[i], out[i])
        a = nn(inp[i], out[i])
        print(a)
        save_weights()
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
#out[4] = np.array([1, -.1])
'''
print(inp)
pickle_out = open('inputs.pickle', 'wb')
pickle.dump(inp, pickle_out)
pickle_out.close()
pickle_out2 = open('outputs.pickle', 'wb')
pickle.dump(out, pickle_out2)
pickle_out2.close()'''
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


'''heldprice = holdprice(30600, 500)
pickle_out2 = open('heldprice.pickle', 'wb')
pickle.dump(heldprice, pickle_out2)
pickle_out2.close()'''
pickle_in2 = open('heldprice.pickle', 'rb')
heldprice = pickle.load(pickle_in2)
print(heldprice)
