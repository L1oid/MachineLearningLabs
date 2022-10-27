import pandas as pd

print("Ex 1)")
polit = pd.read_csv("polit.csv").dropna()
print(polit)

print("Ex 2)")
print(polit[polit["fh09"] > 5])

print("Ex 3)")
print(polit[polit["afri"] & (polit["fparl08"] > 30)])

print("Ex 4)")
print(polit[(polit["afri"] | polit["lati"]) & (polit["polity09"] >= 8)])

print("Ex 5)")
polit["corr_round"] = polit["corr0509"].round(2)
print(polit.iloc[:, -2:])

print("Ex 6)")
def table3(fh_index):
    if fh_index >= 1 and fh_index <= 2.5:
        return "free"
    if fh_index >= 3.0 and fh_index <= 5.0:
        return "partly free"
    if fh_index >= 5.5 and fh_index <= 7.0:
        return "not free"

polit["fh_status"] = polit["fh09"].map(table3)
print(polit[["fh09", "fh_status"]])

print("Ex 7)")
groups = polit.groupby(["fh_status"])
fh_statuses = polit["fh_status"].unique()
for status in fh_statuses:
    group = groups.get_group(status)
    min_gini = group["gini"].min()
    max_gini = group["gini"].max()
    avg_gini = group["gini"].mean()
    print("\nStatus:", status, "\nMin:", min_gini, "\nMax:", max_gini, "\nAvg:", avg_gini)

print("Ex 8)")
groups = polit.groupby(["fh_status"])
fh_statuses = polit["fh_status"].unique()
for status in fh_statuses:
    new_dataframe = groups.get_group(status)
    new_dataframe.to_csv(f"{status}.csv")
