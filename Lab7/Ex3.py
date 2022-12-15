from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
import numpy as np

from sklearn.datasets import load_boston
from sklearn.preprocessing import scale


# Ex 1
boston = load_boston()

x_train = boston.data
y_train = boston.target

# Ex 2
x_train_after_scale = scale(x_train)

# Ex 3
kf = KFold(n_splits=5, random_state=42, shuffle=True)

scores = {}
for p in np.linspace(1, 10, num=200):
    knr = KNeighborsRegressor(p=p, n_neighbors=5, weights="distance")
    score = cross_val_score(knr, x_train_after_scale,
                            y_train, cv=kf, scoring="neg_mean_squared_error")
    scores[p] = np.mean(score)

# Ex 4
max_val = max(scores, key=scores.__getitem__)
print(f"{max_val}: {scores[max_val]}")