import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


def f(x):
    return 5 * x + np.random.random(x.shape) * 10


X = np.arange(-10, 11, 1).reshape(-1, 1)
y = f(X)

plt.scatter(X, y)
plt.show()

lr = LinearRegression()
lr.fit(X, y)
y_pred = lr.predict(X)

print("Угловой коэф: ", lr.coef_[0])
print("Пересечение: ", lr.intercept_)
print("Точность: ", lr.score(X, y))

plt.plot(X, y_pred)
plt.scatter(X, y)
plt.show()
