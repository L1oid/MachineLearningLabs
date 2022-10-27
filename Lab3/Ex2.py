import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = [["Вжик", "Zipper the Fly", "fly", "0.7"],
        ["Гайка", "Gadget Hackwrench", "mouse", None],
        ["Дейл", "Dale", "chipmunk", "1"],
        ["Рокфор", "Monterey Jack", "mouse", "0.8"],
        ["Чип", "Chip", "chipmunk", "0.2"]]

print("Ex 1)")
dataframe = pd.DataFrame(data)
print(dataframe)
print(dataframe[3].dtype)
dataframe[3] = dataframe[3].astype("float")
print(dataframe[3].dtype)

print("Ex 2)")
print(len(dataframe.index))

print("Ex 3)")
print(dataframe[3].count())

print("Ex 4)")
print(dataframe.loc[2][1])

print("Ex 5)")
dataframe1 = dataframe.loc[1:3, 0:2]
print(dataframe1)

print("Ex 6)")
dataframe.columns = ["ru_name", "en_name", "class", "cheer"]
print(dataframe)

print("Ex 7)")
dataframe["logcheer"] = dataframe["cheer"].apply(np.log)
print(dataframe)

print("Ex 8)")
x = dataframe["class"].value_counts().index
y = dataframe["class"].value_counts().values

plt.title("class frequencies")
plt.xlabel("class")
plt.ylabel("frequency")
plt.yticks((min(y) - 1, max(y), 1))
plt.bar(x, y)
plt.show()