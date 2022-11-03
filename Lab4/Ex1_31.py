import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('tips')
sb.regplot(x="total_bill", y="tip", data=df)
sb.lmplot(x="total_bill", y="tip", data=df)
plt.show()
