import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv("bikes_rent.csv")

g = sb.pairplot(data=df, y_vars=["cnt"])
g.fig.set_size_inches(18, 3)
plt.show()

print(df.corr())

df = df.drop(["atemp", "windspeed(mph)"], axis=1)

x = df.drop("cnt", axis=1)
y = df["cnt"]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
lr = LinearRegression()
lr.fit(x_train, y_train)

print(lr.score(x_test, y_test))