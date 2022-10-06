import matplotlib.pyplot as plt

plt.title("Two on more lines with different widths and colors suitable legends")
plt.ylabel("y - axis")
plt.xlabel("x - axis")

plt.plot([10, 20, 30], [20, 40, 10], color = 'blue', linewidth = 3)
plt.plot([10, 20, 30], [40, 10, 30], color = 'red', linewidth = 5)

plt.legend(("line1-width-3", "line2-width-5"))
plt.show()