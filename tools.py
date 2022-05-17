from neural_net import *

# this trains neural net
start = timer()
for b in range(2):
    for i in range(len(out.keys())):
        train(1, inp[i], out[i])
        a = nn(inp[i], out[i])
        print(a)
for i in range(len(out.keys())):
    print(i, output(inp[i]))
    print(out[i])
end = timer()
print(end-start)

# change held price for stop loss & take profit
'''heldprice = holdprice(30400, 1000)
pickle_out2 = open('heldprice.pickle', 'wb')
pickle.dump(heldprice, pickle_out2)
pickle_out2.close()
'''
