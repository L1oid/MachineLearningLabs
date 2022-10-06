import matplotlib.pyplot as plt

plt.title("Display marker")
plt.ylabel("y - axis")
plt.xlabel("x - axis")

plt.plot([1, 4, 5, 6, 7], [2, 6, 3, 6, 3], linestyle = '-.', color = 'red')
plt.scatter([1, 4, 5, 6, 7], [2, 6, 3, 6, 3], color = 'blue')

plt.show()