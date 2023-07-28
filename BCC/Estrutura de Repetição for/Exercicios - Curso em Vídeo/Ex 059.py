soma_pares = 0

for i in range(0, 6):
    x = int(input())
    if x % 2 == 0:
        soma_pares += x


print(soma_pares)