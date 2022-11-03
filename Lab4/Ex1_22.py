import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('iris')
sb.stripplot(x="species", y="petal_length", data=df, jitter=True)
plt.show()
