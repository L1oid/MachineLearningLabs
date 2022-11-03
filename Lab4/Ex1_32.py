import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('tips')
sb.lmplot(x="size", y="tip", data=df)
plt.show()
