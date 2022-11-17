import pandas as pd
from statsmodels.stats.weightstats import _tconfint_generic
import numpy as np

df = pd.read_csv("14water.txt", sep="\t")
print(df.head())

# Ex1
print("North")
print(df[df["location"] == "North"].describe())
print("South")
print(df[df["location"] == "South"].describe())

# Ex2
print()
df_north = df[df["location"] == "North"]
df_south = df[df["location"] == "South"]

mort_mean_n = df_north["mortality"].mean()
mort_mean_s = df_south["mortality"].mean()

mort_mean_std_n = df_north["mortality"].std() / np.sqrt(df_north["mortality"].shape[0])

mort_mean_std_s = df_south["mortality"].std() / np.sqrt(df_south["mortality"].shape[0])

print("North 95%:", _tconfint_generic(mort_mean_n, mort_mean_std_n,df_north["mortality"].shape[0] - 1, 0.05, "two-sided"))

print("South 95%:", _tconfint_generic(mort_mean_s, mort_mean_std_s,df_south["mortality"].shape[0] - 1, 0.05, "two-sided"))

# Ex3
print()
df_north = df[df["location"] == "North"]
df_south = df[df["location"] == "South"]

mort_mean_n = df_north["hardness"].mean()
mort_mean_s = df_south["hardness"].mean()

mort_mean_std_n = df_north["hardness"].std() / np.sqrt(df_north["hardness"].shape[0])

mort_mean_std_s = df_south["hardness"].std() / np.sqrt(df_south["hardness"].shape[0])

print("North 95%:", _tconfint_generic(mort_mean_n, mort_mean_std_n, df_north["hardness"].shape[0] - 1, 0.05, "two-sided"))

print("South 95%:", _tconfint_generic(mort_mean_s, mort_mean_std_s, df_south["hardness"].shape[0] - 1, 0.05, "two-sided"))
