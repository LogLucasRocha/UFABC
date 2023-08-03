natural_1 = int(input())
natural_2 = int(input())
soma_1 = 0
soma_2 = 0

for c in range(1, natural_1):
    if natural_1 % c == 0:
        soma_1 += c

for c in range(1, natural_2):
    if natural_2 % c == 0:
        soma_2 += c

if (soma_1 == natural_2) and (soma_2 == natural_1):
    print('amigos')
else:
    print('nao amigos')

