import numpy as np

data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])

mean = np.mean(data)
var = np.var(data)
std = np.std(data)

low, high = mean-std, mean+std
count = len([x for x in data if low < x < high])
print((count/len(data)*100))
