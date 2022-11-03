import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('iris')
sb.kdeplot(df['petal_length'])
plt.show()
