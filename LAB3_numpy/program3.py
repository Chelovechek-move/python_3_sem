import numpy as np
import matplotlib.pyplot as plt
import time

I = np.eye(50)
A = np.eye(50)
A[0, -1] = -1.
for i in range(49):
    A[i + 1, i] = -1.

with open("start_dat.txt", 'r') as file:
    U = np.array([float(el) for el in file.read().split()])

data_x = np.linspace(0, 50)

for i in range(255):
    plt.ion()                       # interactive mode will be on
    plt.clf()                       # clear the current figure
    U = U @ (I - 0.5 * A)           # @ means matrix multiplication
    plt.axis([0, 50, 0, 10])
    plt.grid(True)
    plt.plot(data_x, U)
    plt.draw()                          # updating plot
    plt.gcf().canvas.flush_events()     # updating plot
    plt.show()
    time.sleep(0.01)

plt.ioff()                          # interactive mode will be off
