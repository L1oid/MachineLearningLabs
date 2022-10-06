import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

color_rectangle = ["Red", "Black", "Green", "Blue", "Yellow", "Turquoise"]
ax.bar(["Java", "Python", "PHP", "JavaScript", "C#", "C++"], [22, 16.5, 8.9, 8, 7.7, 6.9], color = color_rectangle, edgecolor = 'Black', linewidth = 1)

plt.title("PopularitY of Programming Language\n Worldwide, Oct 2017 compared to a year ago")
plt.ylabel("Popularity")
plt.xlabel("Languages")

plt.minorticks_on()
plt.grid(which='major',color = 'red', linewidth = 1)
plt.grid(which='minor', color = 'grey', linestyle = ':', linewidth = 1)

plt.show()