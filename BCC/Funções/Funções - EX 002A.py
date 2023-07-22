import matplotlib.pyplot as plot
import numpy as np

x = np.arange(0, 8.1, 0.1)
ax = x ** 3 + 3 * x ** 2 - 54

plot.plot(x, ax)
plot.grid(True, which="both")
plot.show()
