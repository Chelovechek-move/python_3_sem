import pandas as pd
import matplotlib.pyplot as plt

ejudge = pd.read_html("results_ejudge.html")[0]
excel = pd.read_excel("students_info.xlsx")

data = pd.merge(excel, ejudge, how="left", right_on="User", left_on="login")
tasks_by_fac_group_ave = [data[data["group_faculty"] == i]['Solved'].mean() for i in data["group_faculty"].unique()]
tasks_by_inf_group_ave = [data[data["group_out"] == i]['Solved'].mean() for i in data["group_out"].unique()]

plt.subplot(1, 2, 1)
plt.title("Average number of solved tasks for faculty groups")
plt.bar([i for i in data["group_faculty"].unique()], tasks_by_fac_group_ave, width=0.2,
        color=['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black'], alpha=0.7, zorder=2)

plt.subplot(1, 2, 2)
plt.title("Average number of solved tasks for informatics groups")
plt.bar([i for i in data["group_out"].unique()], tasks_by_inf_group_ave, width=0.2,
        color=['red', 'blue', 'green', 'orange', 'yellow', 'purple', 'black'], alpha=0.7, zorder=2)
plt.show()

print("Fac_groups: ", end=" ")
for gr_faculty in data["group_faculty"][(data["G"] > 10) | (data['H'] > 10)]:
    print(gr_faculty, end="  ")
print()
print("            ", end=" ")
for i in range(len(data["group_faculty"][(data["G"] > 10) | (data['H'] > 10)])):
    print("|", end="  ")
print()
print("Inf_groups: ", end=" ")
for gr_info in data["group_out"][(data["G"] > 10) | (data['H'] > 10)]:
    print(gr_info, end=" ")
print()
