import pandas as pd
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import scale

# Ex 1
df = pd.read_csv("wine.data")
print(df.head())

# Ex 2
x_train = df.iloc[:, 1:]
y_train = df.iloc[:, 0]

# Ex 3
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Ex 4

scores = []
for k in range(1, 51):
    knc = KNeighborsClassifier(n_neighbors=k)
    scores.append(cross_val_score(
        knc, x_train, y_train, cv=kf, scoring="accuracy"))

acc_df = pd.DataFrame(scores, index=range(1, 51))
print(acc_df.mean(axis=1).sort_values(ascending=False)[:10])

# Ex 5
x_train_after_scale = scale(x_train)

scores = []
for k in range(1, 51):
    knc = KNeighborsClassifier(n_neighbors=k)
    scores.append(cross_val_score(
        knc, x_train_after_scale, y_train, cv=kf, scoring="accuracy"))

acc_df = pd.DataFrame(scores, index=range(1, 51))
print(acc_df.mean(axis=1).sort_values(ascending=False)[:10])