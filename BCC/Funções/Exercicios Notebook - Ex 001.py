import numpy as np
import matplotlib.pyplot as plot

x = np.arange(-2, 4.1, 0.1)
y = x ** 4 - 4 * x ** 3 + x ** 2 + 1

plot.plot(x, y)
plot.grid(True, which="both")
plot.show()

