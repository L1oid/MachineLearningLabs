import pandas as pd

print("Ex 1)")
series = pd.Series(range(1, 6), ["a", "b", "c", "d", "e"])
print(series)

print("Ex 2)")
print(series["d"])

print("Ex 3)")
print(series[1])

print("Ex 4)")
series["f"] = 6
print(series)

print("Ex 5)")
print(series[2:5])

print("Ex 6)")
dataframe = pd.DataFrame([[1, 2], [5, 3], [3.7, 4.8]], columns=["col1", "col2"])
print(dataframe)

print("Ex 7)")
print(dataframe["col1"][2])

print("Ex 8)")
dataframe["col2"][1] = 9
print(dataframe)

print("Ex 9)")
print(dataframe[::][1:3])

print("Ex 10)")
dataframe["col3"] = dataframe["col1"] * dataframe["col2"]
print(dataframe)