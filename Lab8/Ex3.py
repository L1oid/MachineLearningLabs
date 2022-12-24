import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.ensemble import RandomForestClassifier

# Ex1
df = pd.read_csv('winequality-red.csv')
print(df.head())

# Ex2
df = df.dropna()
x = df.drop(["quality"], axis=1)
y = df.quality
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state = 42)
clf = RandomForestClassifier(random_state=241)
print(clf.fit(x_train, y_train))

# Ex3
y_pred = clf.predict(x_test)
print(classification_report(y_test, y_pred))

# Ex4
plt.bar(df.columns[:-1], clf.feature_importances_)
plt.xticks(rotation=45)
plt.show()
