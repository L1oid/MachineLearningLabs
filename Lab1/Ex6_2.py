import matplotlib.pyplot as plt

fig = plt.figure()

ax11 = fig.add_axes([0.,0.,1.0,1.0])
ax21 = fig.add_axes([0.7,0.5,0.2,0.2])

plt.ylabel("y")
plt.xlabel("x")

ax11.plot([0, 100], [0, 200])
ax21.plot([0, 100], [0, 200])

plt.show()