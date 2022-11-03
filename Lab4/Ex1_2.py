import seaborn as sb

data = sb.load_dataset("iris")
print(data.head())

df = sb.load_dataset('tips')
print(df.head())
