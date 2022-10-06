import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()

vals = [31.3, 24.8, 12.4, 11.3, 10.8, 9.4]
labels = ["Java", "Python", "PHP", "JavaScript", "C#", "C++"]
explode = (0.1, 0, 0, 0, 0, 0.2)

plt.title("PopularitY of Programming Language\n Worldwide, Oct 2017 compared to a year ago", bbox=dict(facecolor='Grey', alpha=0.5))

ax.pie(vals, labels=labels, autopct='%1.1f%%', shadow=True, explode=explode, wedgeprops={'lw':1, 'ls':'-','edgecolor':"k"})

plt.show()