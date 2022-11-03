import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('iris')
sb.barplot(x="species", y="petal_length", data=df)
plt.show()
