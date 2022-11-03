import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('anscombe')
sb.lmplot(x="x", y="y", data=df.query("dataset == 'I'"))
plt.show()
