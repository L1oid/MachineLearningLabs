import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error

X = np.array([258.0, 270.0, 294.0, 320.0, 342.0, 368.0,
             396.0, 446.0, 480.0, 586.0])[:, np.newaxis]
y = np.array([236.4, 234.4, 252.8, 298.6, 314.2,
             342.2, 360.8, 368.0, 391.2, 390.8])

lr = LinearRegression()  # Линейная регрессия
lr.fit(X, y)

X_ = np.arange(250, 600, 10)[:, np.newaxis]  # Точки для предсказания
y_lr = lr.predict(X_)

pr = LinearRegression()

quadratic = PolynomialFeatures(degree=2)
X_quad = quadratic.fit_transform(X)

pr.fit(X_quad, y)

y_pr = pr.predict(quadratic.fit_transform(X_))

# Ex1
# Оцените полученные модели с помощью коэффициента детерминации и MSE. Что можно сказать о качестве моделей?
y_pred = lr.predict(X)
print('Для линейной регрессии: \nMSE:', mean_squared_error(y, y_pred))
print("к. детерминации:", lr.score(X, y))

y_pred = pr.predict(quadratic.fit_transform(X))
print('\nДля полиномиальной регрессии: \nMSE:', mean_squared_error(y, y_pred))
print("к. детерминации:", pr.score(quadratic.fit_transform(X), y))

# Ex2
# Постройте полиномиальную модель, описывающую следующую зависимость:
x = np.array([10, 12, 15, 20, 25, 30, 34, 40, 47, 54, 57])[:, np.newaxis]
y = np.array([80, 75, 70, 63, 65, 70, 76, 85, 90, 92, 87])

plt.scatter(x, y)  # Изображаем точки на графике
plt.show()


def poly(degree):
    pr = LinearRegression()
    quadratic = PolynomialFeatures(degree=degree)
    x_ = np.arange(10, 57.5, 0.5)[:, np.newaxis]
    x_quad = quadratic.fit_transform(x)
    pr.fit(x_quad, y)

    y_pr = pr.predict(quadratic.fit_transform(x_))

    plt.scatter(x, y)
    plt.plot(x_, y_pr)
    plt.show()


poly(4)

# Ex3
# Какую степень полинома вы использовали? Попробуйте изменить степень полинома, например, на 2, 5, 15? Как меняется результат?

poly(2)
poly(5)
poly(15)