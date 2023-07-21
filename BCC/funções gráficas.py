import matplotlib.pyplot as plot
import numpy as np

# Estudo de funções gráficas e arrays

# #Primeiro Gráfico
# x = np.arange(0, 2 * math.pi, 0.1)
# f = np.sin(x)
# plot.plot(x, f)
# plot.title("Seno de X")
# plot.xlabel("X")
# plot.ylabel("Y")
# plot.grid(True, which="both")
# plot.show()

# Segundo Gráfico com raízes reais

x = np.arange(1, 4.1, 0.1)
y = x ** 2 - 5 * x + 6
plot.plot(x, y)
plot.title("y = x^2 - 5x + 6")
plot.xlabel("X")
plot.ylabel("Y")
plot.grid(True, which="both")
plot.plot(2, 0, 'r*')
plot.plot(3, 0, 'g*')
plot.show()

