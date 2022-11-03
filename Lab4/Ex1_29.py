import matplotlib.pyplot as plt
import seaborn as sb

df = sb.load_dataset('titanic')
sb.countplot(x="class", data=df, palette="Blues")
plt.show()
