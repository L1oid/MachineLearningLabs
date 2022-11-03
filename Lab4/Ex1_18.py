import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('iris')
sb.jointplot(x='petal_length', y='petal_width', data=df)
plt.show()
