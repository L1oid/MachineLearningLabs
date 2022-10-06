import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

ax.bar(["Java", "Python", "PHP", "JavaScript", "C#", "C++"], [22, 16.5, 8.9, 8, 7.7, 6.9], color = "Blue", edgecolor = 'Black', linewidth = 1)
ax.text("Java", 22.3, '22.200000', fontsize=8, horizontalalignment = "center")
ax.text("Python", 16.8, '17.600000', fontsize=8, horizontalalignment = "center")
ax.text("PHP", 9.2, '8.800000', fontsize=8, horizontalalignment = "center")
ax.text("JavaScript", 8.3, '8.000000', fontsize=8, horizontalalignment = "center")
ax.text("C#", 8.0, '7.700000', fontsize=8, horizontalalignment = "center")
ax.text("C++", 7.2, '6.700000', fontsize=8, horizontalalignment = "center")

plt.title("PopularitY of Programming Language\n Worldwide, Oct 2017 compared to a year ago")
plt.ylabel("Popularity")
plt.xlabel("Languages")

plt.minorticks_on()
plt.grid(which='major',color = 'red', linewidth = 1)
plt.grid(which='minor', color = 'grey', linestyle = ':', linewidth = 1)

plt.show()