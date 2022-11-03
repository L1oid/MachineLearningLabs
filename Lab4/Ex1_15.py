import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('iris')
sb.displot(df['petal_length'], kde=False)
plt.show()
