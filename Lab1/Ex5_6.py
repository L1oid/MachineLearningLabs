import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

columns_text = ["G0", "G1", "G2", "G3", "G4", "G5"]

ax.bar([1 - 0.3/2, 2 - 0.3/2, 3 - 0.3/2, 4 - 0.3/2, 5 - 0.3/2], [22, 30, 33, 29, 26], color = "Green", edgecolor = 'Black', linewidth = 1, width = 0.3)
ax.bar([1 + 0.3/2, 2 + 0.3/2, 3 + 0.3/2, 4 + 0.3/2, 5 + 0.3/2], [25, 32, 29, 35, 28], color = "Red", edgecolor = 'Black', linewidth = 1, width = 0.3)

plt.title("PopularitY of Programming Language\n Worldwide, Oct 2017 compared to a year ago")
plt.ylabel("Popularity")
plt.xlabel("Languages")
ax.set_xticklabels(columns_text)

ax.legend(("Men", "Women"))

plt.show()