import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('iris')
sb.boxplot(x="species", y="petal_length", data=df)
plt.show()

df = sb.load_dataset('iris')
sb.boxplot(data=df, orient="h")
plt.show()
