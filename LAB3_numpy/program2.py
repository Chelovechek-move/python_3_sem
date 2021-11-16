import numpy as np
import matplotlib.pyplot as plt

with open("signal01.dat", "r") as file:
    data_y = np.array([float(el) for el in file.read().split()])

data_x = np.linspace(0, 100, data_y.size)
data_y_new = np.array([])

sum_data = 0
n = 10

for i in range(data_y.size):
    if i + 1 <= n:
        sum_data = (data_y[:i+1].sum()) / (i + 1)
        data_y_new = np.append(data_y_new, sum_data)
    else:
        sum_data = (data_y[i-10:i].sum()) / n
        data_y_new = np.append(data_y_new, sum_data)

plt.subplot(1, 2, 1)
plt.title("Сырой сигнал")
plt.grid(True)
plt.plot(data_x, data_y)

plt.subplot(1, 2, 2)
plt.title("После фильтра")
plt.grid(True)
plt.plot(data_x, data_y_new)
plt.show()
