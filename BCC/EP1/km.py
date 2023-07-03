valor = int(input())

cedulas = [100, 50, 20, 10, 5, 2, 1]
quantidades = []

for cedula in cedulas:
    quantidade = valor // cedula
    quantidades.append(quantidade)
    valor %= cedula

resultado = ", ".join(f"{q} de {c}" for q, c in zip(quantidades, cedulas))
print(resultado)