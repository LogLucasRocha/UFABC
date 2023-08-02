inicio = int(input())
contador = 0

while inicio >= contador:
    inicio -= contador
    print(f'Faltam {inicio} segundos')
    contador += 2
print('Acabou')