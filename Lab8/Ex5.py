import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import log_loss
import math

# Ex1
df = pd.read_csv('gbm-data.csv')
y = df.loc[:, 'Activity']
X = df.drop('Activity', axis = 1)
X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size = 0.8, random_state = 241)

# Ex2
def sig(y_pred):
    return 1. / (1. + math.e ** -y_pred)

for rate in [1., 0.5, 0.3, 0.2, 0.1]:
    print('Rate: ' + str(rate))
    clf = GradientBoostingClassifier(learning_rate = rate, n_estimators=250, verbose=False, random_state=241)
    clf.fit(X_train, y_train)
    test_loss = [log_loss(y_test, sig(y_pred)) for y_pred in clf.staged_decision_function(X_test)]
    train_loss = [log_loss(y_train, sig(y_pred)) for y_pred in clf.staged_decision_function(X_train)]
    print('Min @test:'),
    min_loss = min(test_loss)
    print([tuple_ for tuple_ in zip(range(1, len(test_loss)), test_loss) if tuple_[1] == min_loss])
    plt.figure()
    plt.plot(test_loss, 'r', linewidth=2)
    plt.plot(train_loss, 'g', linewidth=2)
    plt.legend(['test', 'train'])
    plt.show()

# Ex5
clf = GradientBoostingClassifier(n_estimators=37, verbose=False, random_state=241)
clf.fit(X_train, y_train)
test_loss = [log_loss(y_test, sig(y_pred)) for y_pred in clf.staged_decision_function(X_test)]

print(test_loss[-1])
print(log_loss(y_test, clf.predict_proba(X_test)))
