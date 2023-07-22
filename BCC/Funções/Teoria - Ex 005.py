import numpy as np
import matplotlib.pyplot as plot

x1 = np.arange(-25, 25.1, 0.1)
y1 = np.cos(x1)

plot.plot(x1, y1)

x2 = np.arange(-15, 15.1, 0.1)
y2 = np.sqrt(226 - x2 ** 2)

plot.plot(x2, y2)

plot.show()