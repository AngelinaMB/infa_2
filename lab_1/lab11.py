import numpy
import numpy as np
x = [1, 10, 100]
y = np.log(np.exp(1 / np.sin(x) + 1) / (5 / 4 + 1 / np.power(x, 15))) / np.log(1 + np.power(x, 2))
print(y)
