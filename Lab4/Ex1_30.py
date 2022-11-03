import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('titanic')
sb.pointplot(x="sex", y="survived", hue="class", data=df)
plt.show()
