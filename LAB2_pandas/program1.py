import pandas as pd

data = pd.read_csv("transactions.csv")
OK_data = data[data['STATUS'] == 'OK']
print(f"The three largest payments actually made:\n{OK_data.loc[OK_data['SUM'].nlargest(3).index]}\n")
print(f"The total amount of payments actually made to Umbrella, Inc:\n{OK_data.loc[OK_data['CONTRACTOR'] == 'Umbrella, Inc']['SUM'].sum()}\n")
