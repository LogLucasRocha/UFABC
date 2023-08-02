inicio = int(input())
contador = 0

while inicio >= contador:
    inicio = inicio - contador
    print('Faltam {} segundos'.format(inicio))
    contador = contador + 2
print('Acabou')