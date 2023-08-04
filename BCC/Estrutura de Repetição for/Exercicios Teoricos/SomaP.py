n = int(input('Digite um n > 0: '))
soma_p = 0

if n > 0:
    for i in range(1, n+1):
        i = i ** 2
        soma_p += i
    print(soma_p)
else:
    print('input inválido!')