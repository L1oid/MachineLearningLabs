import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot()

x = np.arange(-3, 3, 0.1)
y = np.log((x ** 2 + 1) * np.exp(-np.abs(x) / 10) / np.log(1 + np.tan(1 / (1 + np.sin(x) ** 2))))

ax.plot(x, y, color = 'black')

plt.title("Функция")
plt.ylabel("Ось Y")
plt.xlabel("Ось X")

plt.minorticks_on()
plt.grid(which='major',color = 'grey', linewidth = 2)
plt.grid(which='minor', color = 'grey', linestyle = ':', linewidth = 1)

plt.show()