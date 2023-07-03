a = int(input())
b = int(input())
c = int(input())

v = a * b * c
valor_de_V = "{:.2f}".format(v)

d = (a ** 2 + b ** 2 + c ** 2) ** 0.5
valor_de_d = "{:.2f}".format(d)

print(f'Volume: {valor_de_V} ' f'Diagonal: {valor_de_d}')
