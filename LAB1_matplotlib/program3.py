import matplotlib.pyplot as plt
import numpy as np
import csv


def sum_arr(k):
    sum_prep = np.zeros(len(prep_mark))
    sum_group = np.zeros(len(group_mark))
    for i in range(k):
        sum_prep += prep_mark[:, i]
        sum_group += group_mark[:, i]
    return sum_prep, sum_group


fig, axs = plt.subplots(nrows=1, ncols=2)
preps, groups, marks = [], [], []
colors = ["#FF0000", "#FF3333", "#FF8000", "#FFB266", "#FFFF00", "#FFFF99", "#99FF99", "#00FF00"]

try:
    with open("students.csv", 'r') as file:
        csv_file = csv.reader(file, delimiter=';')
        for line in csv_file:
            preps.append(int(line[0][-1]))
            groups.append(int(line[1][-1]))
            marks.append(int(line[2]))
except FileNotFoundError:
    print("File not found!")
    print("Type the correct name!")
    exit()

print(preps)
print(marks)
print(groups)

prep_mark = np.array([np.zeros(8) for i in range(7)])
group_mark = np.array([np.zeros(8) for i in range(6)])
x_preps = ["prep" + str(j + 1) for j in range(7)]
x_groups = [str(750 + j + 1) for j in range(6)]

for i in range(len(preps)):
    prep_mark[preps[i] - 1][marks[i] - 3] += 1
    group_mark[groups[i] - 1][marks[i] - 3] += 1

print(prep_mark)

for i in range(0, 8):
    axs[0].bar(x_preps, prep_mark[:, i], bottom=sum_arr(i)[0], label=str(i + 3),
               color=colors[i])
    axs[1].bar(x_groups, group_mark[:, i], bottom=sum_arr(i)[1], label=str(i + 3),
               color=colors[i])

plt.subplot(121)
plt.title("Marks per prep")
plt.subplot(122)
plt.title("Marks per group")
plt.legend(bbox_to_anchor=(1, 1))
plt.show()
