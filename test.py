import pickle
import numpy as np
wh_in = open('wh.pickle', 'rb')
wh = pickle.load(wh_in)
array = np.zeros(shape=13)
array[0] = float(wh["0"]) / 100000
array[1] = float(wh["1"])
array[2] = float(wh["2"])
array[3] = float(wh["3"])
array[4] = float(wh["4"])
array[5] = float(wh["5"])
array[6] = float(wh["6"])
array[7] = float(wh["7"]) 
array[8] = float(wh["8"]) / 100000
array[9] = float(wh["9"]) / 100000
array[10] = float(wh["10"]) / 100000
array[11] = float(wh["11"]) / 100000
array[12] = float(wh["12"]) / 100000000

print(array)


# {'EMA 21': '38500.21186664863', 'Yellow Diamond': '0', 'Trend Change': '0', 'Green Dot': '0', 'Red X': '0', 'Manipulation': '0', 'Red Diamond': '0', 'Blood Diamond': '0', 'Close': '39062.5', 'Open': '38947', 'High': '39077.5', 'Low': '38946.5', 'Volume': '23983115'}
