# (b) Escreva em qual (quais) intervalos y2(x) é maior ou igual à y1(x), e em qual (quais) intervalos y2(x) é menor
# ou igual à y1(x).(b) Escreva em qual (quais) intervalos y2(x) é maior ou igual à y1(x), e em qual (quais)
# intervalos y2(x) é menor ou igual à y1(x).

import numpy as np
import matplotlib.pyplot as plot

x = np.arange(-2, 2.1, 0.1)
y1 = np.exp(x)
y2 = 3 * (x ** 2)

plot.plot(x, y1)
plot.plot(x, y2)
plot.show()

# R = {[-2, -0.5 e 1, 2], [-0.5, 1]}
