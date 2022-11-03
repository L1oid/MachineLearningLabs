import matplotlib.pyplot as plt
import seaborn as sb

iris = sb.load_dataset("iris")
ax = sb.pairplot(iris)
plt.show()
