import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
from sklearn.model_selection import GridSearchCV

# Ex1
df = pd.read_csv('diabetes.csv')
print(df.head())

# Ex2
df = df.dropna()
x = df.drop(["Outcome"], axis=1)
y = df.Outcome
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.4, random_state = 42)

# Ex3
clf = DecisionTreeClassifier(random_state=241)
print(clf.fit(x_train, y_train))

# Ex4
y_pred = clf.predict(x_test)
print(classification_report(y_test, y_pred))

# Ex5
parameters = {'max_depth': range(3, 100, 1)}
print(parameters)

# Ex6
dtc = DecisionTreeClassifier()
grid = GridSearchCV(dtc, parameters)
grid.fit(x_train, y_train)
print(grid.best_estimator_)
