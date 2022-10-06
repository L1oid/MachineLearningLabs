import matplotlib.pyplot as plt

plt.title("Closing stock value of Alphabet Inc.")
plt.ylabel("Closing value")
plt.xlabel("Date")

plt.plot(["2016-10-03", "2016-10-04", "2016-10-05", "2016-10-06", "2016-10-07"], [772.5, 776.4, 776.5, 776.9, 775.1], color = 'red')
plt.scatter(["2016-10-03", "2016-10-04", "2016-10-05", "2016-10-06", "2016-10-07"], [772.5, 776.4, 776.5, 776.9, 775.1], color = 'red')
plt.minorticks_on()
plt.grid(which='major',color = 'red', linewidth = 1)
plt.grid(which='minor', color = 'red', linestyle = ':')
plt.yticks([772.5, 773.0, 773.5, 774.0, 774.5, 775.0, 775.5, 776.0, 776.5, 777.0])

plt.show()