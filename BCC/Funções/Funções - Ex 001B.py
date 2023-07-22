import matplotlib.pyplot as plot
import numpy as np

x = np.arange(0, 20.1, 0.1)
y = (50 * x) - (48 * x ** 0.9) - 50
plot.plot(x, y)
plot.grid(True, which='both')
plot.title("y = (50 * x) - (48 * (x) ** 0.9) - 50")
plot.xlabel("Carros")
plot.ylabel("Lucro")
plot.show()
