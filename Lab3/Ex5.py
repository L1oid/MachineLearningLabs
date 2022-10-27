import pandas as pd

dataframe = pd.read_csv("vgsales.csv")

print("Ex 1)")
print(dataframe["Platform"].unique())

print("Ex 2)")
metacritic_dataframe = pd.read_csv("metacritic_games.csv", usecols=["name", "platform", "rating"])
metacritic_dataframe.rename(columns={"name": "Name", "platform": "Platform", "rating": "Metacritic_rating"}, inplace=True)
dataframe1 = dataframe.copy(deep=True)
dataframe1 = dataframe1.merge(metacritic_dataframe)
print(dataframe1)

print("Ex 3)")
dataframe2 = dataframe1[(dataframe1["Metacritic_rating"] == "M") & (dataframe1["Year"] >= 2012)]
print(dataframe2)

print("Ex 4)")
print(dataframe2.describe())

print("Ex 5)")
genres = dataframe["Genre"].unique()

def vowel(word):
    vowels = ["a", "e", "i", "u", "y", "o"]
    count = 0
    for symbol in word.lower():
        if count == 3:
            return True
        if symbol in vowels:
            vowels.remove(symbol)
            count += 1
    return False

genres = list(filter(vowel, genres))
for genre in genres:
    count = dataframe["Genre"].value_counts()[genre]
    print(genre, " \t-", count)