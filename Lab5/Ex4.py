import pandas as pd
import numpy as np
import statistics
import seaborn as sns
import matplotlib.pyplot as plt

# Ex1
df = pd.read_csv("CAR DETAILS FROM CAR DEKHO.csv", sep=",",)
print(df.head(10))

# Ex2
df.info(memory_usage="deep")

# Ex4
df_p = df["selling_price"]
print("Параметры для цены:")

mean = np.mean(df_p)
print("Среднее: ", mean)

hmean = statistics.harmonic_mean(df_p)
print("Гармоническое среднее: ", hmean)

gmean = statistics.geometric_mean(df_p)
print("Среднее геометрическое: ", gmean)

median = statistics.median(df_p)
print("Медиана: ", median)

mode = statistics.mode(df_p)
print("Мода: ", mode)

var = statistics.variance(df_p)
print("Дисперсия: ", var)

std = statistics.stdev(df_p)
print("Среднеквадратичное отклонение: ", std)

skew = df_p.skew()
print("Смещение: ", skew)

ptp = np.ptp(df_p)
print("Диапазон: ", ptp)

result = df_p.describe()
print("Сводка: ")
print(result)

# Ex5
sns.distplot(df["selling_price"])
plt.show()

plt.title("Boxplot of price by transmission and fuel type")
sns.boxplot(y="selling_price", x="transmission", hue="fuel", data=df)
plt.show()

# Ex6
corrmat = df.corr()
f, ax = plt.subplots(figsize=(12, 9))

sns.heatmap(corrmat, vmax=.8, square=True, ax=ax)
plt.show()

k = 10
output = "selling_price"
top10_attr = corrmat.nlargest(k, output).index
top10_mat = corrmat.loc[top10_attr, top10_attr]
fig, ax = plt.subplots(figsize=(8, 6))
sns.set(font_scale=1.25)
sns.heatmap(top10_mat, annot=True, annot_kws={'size': 12}, square=True)
plt.show()
