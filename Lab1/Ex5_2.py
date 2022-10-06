import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

ax.barh(["Java", "Python", "PHP", "JavaScript", "C#", "C++"], [22, 16.5, 8.9, 8, 7.7, 6.9], color = 'Green', edgecolor = 'Black', linewidth = 1)

plt.title("PopularitY of Programming Language\n Worldwide, Oct 2017 compared to a year ago")
plt.ylabel("Languages")
plt.xlabel("Popularity")

plt.minorticks_on()
plt.grid(which='major',color = 'red', linewidth = 1)
plt.grid(which='minor', color = 'grey', linestyle = ':', linewidth = 1)

plt.show()