import numpy as np
import matplotlib.pyplot as plot
import math

x = np.arange(0, 96.1, 0.1)
y = 26 + 5 * np.cos((math.pi / 12) * x) + 4 * math.pi / 3

plot.plot(x, y)
plot.show()

