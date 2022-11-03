import matplotlib.pyplot as plt
import numpy as np
import seaborn as sb


def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 5):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)


sb.set()
sinplot()
plt.show()
