import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LassoCV
from sklearn.linear_model import RidgeCV

# Ex 1
# Загрузите данные в DataFrame, используя функцию read_csv.
df = pd.read_csv("house_price.csv")
print(df.head())

# Ex 2
# Сколько строк и столбцов в данных? Есть ли пропуски? Для ответа навопросы используйте метод info().
print(df.info())

# Ex 3
# Для выполнения задания в наборе данных необходимо оставить только числовые признаки.
numeric_dtypes = ['int64', 'float64']
numerics = []
for i in df.columns:
    if df[i].dtype in numeric_dtypes:
        numerics.append(i)
df = df[numerics]
print(df)

# Ex 4
# Удалите столбец Id и пропущенные значения.

del df["Id"]
df = df.dropna()
print(df)

# Ex 5
# Разделите набор данных на входные данные X (все столбцы кроме SalePrice) и ответы y (столбец SalePrice).
X = df.drop("SalePrice", axis=1)
y = df["SalePrice"]

# Ex 6
# Разделите данные на обучающую и тестовую выборки.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Ex 7
# Обучите модель LassoCV (установите значение гиперпараметра cv самостоятельно).
# Оцените качество полученной модели. Посмотрите на коэффициенты модели.
# Есть ли коэффициенты равные 0? Что это означает?

lasso = LassoCV(cv=5)

lasso.fit(X_train, y_train)
score = lasso.score(X_test, y_test)
print(score)
print(lasso.coef_)

# Ex 8
# Попробуйте использовать L2-регуляризацию, т.е. обучите
# модель RidgeCV. Сравните полученный результат LassoCV и RidgeCV.

ridge = RidgeCV(cv=5)

ridge.fit(X_train, y_train)
score2 = ridge.score(X_test, y_test)
print(f"lasso: {score}, ridge: {score2}")
