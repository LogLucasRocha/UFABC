import math
import numpy as np
import matplotlib.pyplot as plot

# Estudo de funções gráficas e arrays

x = np.arange(0, 2 * math.pi, 0.1)
f = np.sin(x)
plot.plot(x, f)
plot.title("Seno de X")
plot.xlabel("X")
plot.ylabel("Y")
plot.show()
