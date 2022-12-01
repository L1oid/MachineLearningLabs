import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Ex1

df = pd.read_csv("CO2 Emissions_Canada.csv").dropna().drop("Fuel Consumption Comb (mpg)", axis=1)
print(df.head())
print(df.info())

# Ex3

print(df.corr())

x = df.drop(["CO2 Emissions(g/km)", "Make", "Model", "Vehicle Class", "Transmission", "Fuel Type"], axis=1)
y = df["CO2 Emissions(g/km)"]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
lr = LinearRegression()
lr.fit(x_train, y_train)
print(lr.score(x_test, y_test))

# Ex5

test_data = df.iloc[10:15, :-1]
test_co2 = df.iloc[10:15, -1]
print(test_data)

data = test_data.drop(["Make", "Model", "Vehicle Class", "Transmission", "Fuel Type"], axis=1)
test_data["CO2"] = lr.predict(data)

print(test_data["CO2"])

print(test_co2)
