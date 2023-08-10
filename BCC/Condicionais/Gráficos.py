import numpy as np
import matplotlib.pyplot as plt


a = int(input('Digite o valor de a: '))
b = int(input('Digite o valor de b: '))
c = int(input('Digite o valor de c: '))


delta = (b * b) - 4 * a * c

if delta < 0:
    print('Delta não apresenta raízes reais.')
elif delta > 0:
    print(f'O valor de delta é {delta}.')

    r1 = (-b - delta ** 0.5) / (2 * a)
    r2 = (-b + delta ** 0.5) / (2 * a)

    print(f'A raíz 1 é {r1} e a raíz 2 é {r2}.')

    if r1 > r2:
        x = np.arange(r1, r2, 0.01)
        y = (a * x * x) + (b * x) + c
    else:
        x = np.arange(r2, r1, 0.01)
        y = (a * x * x) + (b * x) + c

    plt.plot(x, y)
    plt.show()

else:
    print('A função possui duas raízes identicas e não apresenta gráfico.')