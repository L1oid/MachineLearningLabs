import matplotlib.pyplot as plt
import seaborn as sb

sb.set()
# Набор данных 'чаевые'
tips = sb.load_dataset('tips')
ax = sb.scatterplot(x='total_bill', y='tip', data=tips)
plt.show()