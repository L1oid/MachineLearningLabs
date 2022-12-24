import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Ex1
df = pd.read_csv('train.csv')
print(df.head())

# Ex2 Ex3 Ex4 Ex5
df2 = df[['Survived', 'Pclass', 'Fare', 'Age', 'Sex']].dropna()
train = df2[['Pclass', 'Fare', 'Age', 'Sex']]

def strings_to_int(df, target_column):
    df_mod = df.copy()
    targets_to_rename = df_mod[target_column].unique()
    map_to_int = {name: n for n, name in enumerate(targets_to_rename)}
    df_mod[target_column] = df_mod[target_column].replace(map_to_int)
    return df_mod

x_train = strings_to_int(train, "Sex")
print(x_train.head())

# Ex6
y_train = df2['Survived']
clf = DecisionTreeClassifier(random_state=241)
print(clf.fit(x_train, y_train))

# Ex7
importances = pd.Series(clf.feature_importances_, index = list(x_train))
print(importances)
print(' '.join(importances.sort_values(ascending=False).head(2).index.values))
