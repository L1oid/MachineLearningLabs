import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

width_rectangle = [0.1, 0.2, 0.4, 1, 0.2, 0.3]
ax.bar(["Java", "Python", "PHP", "JavaScript", "C#", "C++"], [22, 16.5, 8.9, 8, 7.7, 6.9], color = "Blue", edgecolor = 'Black', linewidth = 1, width = width_rectangle)

plt.title("PopularitY of Programming Language\n Worldwide, Oct 2017 compared to a year ago")
plt.ylabel("Popularity")
plt.xlabel("Languages")

plt.minorticks_on()
plt.grid(which='major',color = 'red', linewidth = 1)
plt.grid(which='minor', color = 'grey', linestyle = ':', linewidth = 1)

plt.show()