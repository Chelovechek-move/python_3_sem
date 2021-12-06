import numpy as np
import matplotlib.pyplot as plt

wall_position_20_000 = np.loadtxt('wall_position_20_000.txt')
wall_position_12_000 = np.loadtxt('wall_position_12_000.txt')

data_x = np.arange(len(wall_position_20_000))

t_20_000 = np.polyfit(data_x, wall_position_20_000, 4)
f_20_000 = np.poly1d(t_20_000)
data_y_20_000 = np.array([f_20_000(el) for el in data_x])

t_12_000 = np.polyfit(data_x, wall_position_12_000, 4)
f_12_000 = np.poly1d(t_12_000)
data_y_12_000 = np.array([f_12_000(el) for el in data_x])

asymptote_y = np.zeros(2000000 - 1)
asymptote_y = np.array([el + 500 for el in asymptote_y])

fig, ax = plt.subplots()
plt.grid(True)
plt.plot(data_x, asymptote_y, color='#00008B', label='Теоретическая асимптота')
plt.plot(data_x, wall_position_20_000, alpha=0.5, label='Движение стенки при 20 000 шариков')
plt.plot(data_x, wall_position_12_000, alpha=0.5, label='Движение стенки при 12 000 шариков')
plt.plot(data_x, data_y_20_000, label='Аппроксимация при 20 000 шариков')
plt.plot(data_x, data_y_12_000, label='Аппроксимация при 12 000 шариков')
ax.set_ylabel('x')
ax.set_xlabel('N')
plt.legend()
plt.show()
