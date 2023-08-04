n = int(input('Digite um n > 0: '))
soma_r = 0

if n > 0:
    for i in range(1, n+1):
        i = ((i) - (i+1))
        soma_r += i
    print(soma_r)
else:
    print('input inválido!')