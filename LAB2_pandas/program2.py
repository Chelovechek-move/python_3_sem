import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("flights.csv")
names = dict(((el, [0, 0, 0]) for el in data["CARGO"].values))
print(f"names = {names}")
for el in data.to_numpy():
    names.update({el[1]: [names.get(el[1])[0] + 1, el[2] + names.get(el[1])[1], el[3] + names.get(el[1])[2]]})
print(pd.DataFrame(names, index=["Number of flights", "Full cost", "Full mass"]))

data_prices, data_weights, data_number, names_keys = [], [], [], []

for a in names.keys():
    names_keys.append(a)

data_Y = names.values()

for el in data_Y:
    data_number.append(el[0])
    data_prices.append(el[1])
    data_weights.append(el[2])

plt.subplot(1, 3, 1)
plt.title("Prices of all flights")
plt.bar(names_keys, data_prices, width=0.2, color=['red', 'blue', 'green'], alpha=0.7, zorder=2)

plt.subplot(1, 3, 2)
plt.title("Weights of all flights")
plt.bar(names_keys, data_weights, width=0.2, color=['red', 'blue', 'green'], alpha=0.7, label=[names_keys[0],
        names_keys[1], names_keys[2]], zorder=2)

plt.subplot(1, 3, 3)
plt.title("Numbers of flights")
plt.bar(names_keys, data_number,
        width=0.2, color=['red', 'blue', 'green'], alpha=0.7, label=[names_keys[0], names_keys[1], names_keys[2]],
        zorder=2)
plt.show()
