import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('tips')
sb.violinplot(x="day", y="total_bill", hue='sex', data=df)
plt.show()
