import matplotlib.pyplot as plt
import numpy as np
import time

data_x, data_y, n = [], [], 0
try:
    with open("data.txt", "r") as file:
        for line in file:
            data_x = [float(x) for x in line.split()]
            line1 = file.readline()
            data_y = [float(y) for y in line1.split()]
            n += 1
            plt.ion()                   # interactive mode will be on
            plt.clf()                   # clear the current figure
            plt.axis([0, 16, -10, 14])
            plt.title(f'Frame {n}')
            plt.plot(data_x, data_y)
            plt.xticks(np.arange(0, 16, step=2))
            plt.yticks(np.arange(-10, 14, step=2))
            plt.grid(True)
            plt.draw()                          # updating plot
            plt.gcf().canvas.flush_events()     # updating plot
            time.sleep(1)
        data_x = []
        data_y = []
    plt.ioff()
except FileNotFoundError:
    print("File not found!")
    print("Type the correct name!")
    exit()
