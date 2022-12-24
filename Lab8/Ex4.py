import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import cross_val_score
from sklearn.metrics import r2_score
from sklearn.model_selection import KFold

# Ex1
df = pd.read_csv('abalone_csv.csv')
print(df.head())

# Ex2
df['Sex'] = df['Sex'].map(lambda x: 1 if x == 'M' else (-1 if x == 'F' else 0))
print(df.head())

# Ex3
y = df.loc[:, 'Class_number_of_rings']
X = df.drop('Class_number_of_rings', axis = 1)

# Ex4
scores = []
validator = KFold(shuffle=True, random_state=1, n_splits=5)
for n_est in range(1, 51):
    clf = RandomForestRegressor(random_state=1, n_estimators=n_est)
    clf.fit(X, y)
    scores.append((n_est, cross_val_score(clf, X, y, cv=validator, scoring=lambda est, X, y: r2_score(y, est.predict(X))).mean()))

# Ex5
for score in scores:
    if score[1] > 0.52:
        print(score)
        break

# Ex6
plt.plot([score[0] for score in scores], [score[1] for score in scores])
plt.show()
