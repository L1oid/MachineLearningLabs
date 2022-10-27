import pandas as pd
import matplotlib.pyplot as plt

print("Ex 1)")
dataframe = pd.read_csv("la-crimes-sample.csv")
print(dataframe)

print("Ex 2)")
print("cols count = ", len(dataframe.columns))
print("rows count = ", len(dataframe.index))

print("Ex 3)")
dtypes = dataframe.dtypes
dataframe2 = pd.DataFrame(dtypes.items(), columns=["name", "dtype"])
print(dataframe2)

print("Ex 4)")
print(dataframe.nunique())

print("Ex 5)")
print(dataframe.isnull().sum().sum())

print("Ex 6)")
males = dataframe["Victim Sex"].value_counts()["M"]
females = dataframe["Victim Sex"].value_counts()["F"]
print("Male victims =", males, "female victims =", females)
print(females > males)

print("Ex 7)")
top_crime_types = dataframe["Crime Code Description"].value_counts()[:10]
x = top_crime_types.index
y = top_crime_types.values
plt.barh(x, y)
plt.show()

print("Ex 8)")
victims = dataframe.groupby(["Victim Sex"])
males = victims.get_group("M")["Crime Code Description"].value_counts()[:10]
females = victims.get_group("F")["Crime Code Description"].value_counts()[:10]
print("Males:\n", males)
print("\nFemales:\n", females)

print("Ex 9)")
print(dataframe["Victim Descent"].value_counts()[:5])

print("Ex 10)")
areas = dataframe["Area Name"].value_counts()
plt.ylabel("Areas")
plt.xlabel("Crimes count")
plt.barh(areas.index, areas.values)
plt.show()