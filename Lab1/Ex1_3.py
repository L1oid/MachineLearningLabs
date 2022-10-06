import matplotlib.pyplot as plt

plt.title("Plot with two on more lines with different styles")
plt.ylabel("y - axis")
plt.xlabel("x - axis")

plt.plot([10, 20, 30], [20, 40, 10], linestyle = 'dotted', color = 'blue', linewidth = 2)
plt.plot([10, 20, 30], [40, 10, 30], linestyle = ':', color = 'red', linewidth = 4)

plt.legend(("line1-dotted", "line2-dashed"))
plt.show()