import matplotlib.pyplot as plt

data = []
try:
    name_of_file = input()
    with open(name_of_file, "r") as file:
        n = int(file.readline())
        for i in range(0, n):
            line = file.readline()
            data.append([float(x) for x in line.split()])
except FileNotFoundError:
    print("File not found!")
    print("Type the correct name!")
    exit()
size = 8
if name_of_file == "005.dat":
    size = 0.2
data_x, data_y = [x[0] for x in data], [y[1] for y in data]
plt.scatter(data_x, data_y, color='blue', s=size)
plt.title(f'Number of points: {n}')
plt.show()
