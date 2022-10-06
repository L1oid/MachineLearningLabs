import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter

fig = plt.figure()
ax = fig.add_subplot()

plt.title("Элементы изображения")
plt.ylabel("Ось Y")
plt.xlabel("Ось X")

ax.plot([1, 3, 8, 9], [5, 8, 10, 12], color = 'blue')
ax.plot([2, 4, 6, 7], [2, 7, 4, 3], color = 'red')
ax.scatter([0, 2, 3, 5, 8, 9, 1, 6, 7], [0, 5, 6, 3, 4, 9, 2, 7, 8], color = 'Black')
ax.grid(which='major',color = 'grey', linewidth = 1, linestyle = '--')
ax.legend(("Синяя линия", "Красная линия"))

ax.tick_params(axis = 'both',
               which = 'minor',
               labelsize = 7)

ax.xaxis.set_major_locator(ticker.MultipleLocator(2))
ax.xaxis.set_minor_locator(ticker.MultipleLocator(0.5))
ax.xaxis.set_minor_formatter(FormatStrFormatter("%.1f"))


ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

plt.show()