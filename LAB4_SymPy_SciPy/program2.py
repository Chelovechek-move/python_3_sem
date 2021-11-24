import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

data = np.loadtxt("data_2.txt", skiprows=1)
A = data[:-1]
b = data[-1]
x = linalg.solve(A, b)

plt.grid(True)
plt.bar(np.arange(x.shape[0]), x)
plt.show()