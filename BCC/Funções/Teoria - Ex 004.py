import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-5, 2.1, 0.1)
y = x ** 3 - 3 * x ** 2 + 100

plt.plot(x, y)
plt.show()