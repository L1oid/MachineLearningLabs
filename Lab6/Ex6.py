import pandas as pd
from sklearn.metrics import confusion_matrix

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

# Ex1

df = pd.read_csv("classification.csv")
print(df.head())

# Ex2

tp = df[(df["true"] == 1) & (df["pred"] == 1)].shape[0]
fp = df[(df["true"] == 0) & (df["pred"] == 1)].shape[0]
fn = df[(df["true"] == 1) & (df["pred"] == 0)].shape[0]
tn = df[(df["true"] == 0) & (df["pred"] == 0)].shape[0]

print("tp = ", tp, "fp = ", fp, "fn = ", fn, "tn = ", tn)

# Ex3

df_t = df["true"]
df_p = df["pred"]

print(f"Accuracy: ", accuracy_score(df_t, df_p))
print(f"Precision: ", precision_score(df_t, df_p))
print(f"Recall: ", recall_score(df_t, df_p))
print(f"F-мера: ", f1_score(df_t, df_p))

