# Qual é o número de raízes da equação y1(x)=y2(x) no intervalo [–2, 2], ou seja, o número de vezes que y1(x) e y2(x)
# se cruzam no intervalo [–2, 2].

import numpy as np
import matplotlib.pyplot as plot

x = np.arange(-2, 2.1, 0.1)
y1 = np.exp(x)
y2 = 3 * (x ** 2)

plot.plot(x, y1)
plot.plot(x, y2)
plot.show()

# R = {2 vezes}
