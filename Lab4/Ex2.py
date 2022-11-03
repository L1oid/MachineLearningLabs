import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

print("Ex1")
df = pd.read_csv("howpop_train.csv")
print(df)

print("Ex2")
df.drop(
    filter(lambda c: c.endswith("_lognorm"), df.columns),
    axis=1,  # axis = 1: столбцы
    inplace=True,
)  # избавляет от необходимости сохранять датасет
print(df)

print("Ex3")
df["published"] = pd.to_datetime(df.published, yearfirst=True)
print(df)

print("Ex4")
df["year"] = [d.year for d in df.published]
df["month"] = [d.month for d in df.published]
df["dayofweek"] = [d.isoweekday() for d in df.published]
df["hour"] = [d.hour for d in df.published]
print(df)

print("Ex5")
data = df[['year', 'month']]
t = sb.FacetGrid(data, col='year', col_wrap=3)
t.map(sb.countplot, 'month')
plt.show()

print("Ex6")
sb.countplot(x="dayofweek", hue="dayofweek", data=df)
plt.show()

print("Ex9")
sb.violinplot(x=df["dayofweek"], y=df["hour"])
plt.show()
