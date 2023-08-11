import random as rd
import matplotlib.pyplot as plt
import numpy as np

entrada = 1
saldo = 100
rodada = 0
rodadas = []
saldos = []

while saldo > 0:
    numero_sorteado = rd.randint(1, 2)
    if saldo >= 200:
        print('Parabéns! Você atingiu a sua meta diária!')
        print(f'Número de Rodadas: {rodada}')
        break

    elif numero_sorteado == entrada:
        print(f'Você acertou! O número sorteado foi {numero_sorteado}')
        saldo_atual = saldo + 20
        saldo = saldo_atual
        print(f'Saldo atual: R${saldo}')
        rodada += 1
    else:
        print(f'Você errou! O número sorteado foi {numero_sorteado}')
        saldo_atual = saldo - 20
        saldo = saldo_atual
        print(f'Saldo atual: R${saldo}')
        rodada += 1

    rodadas.append(rodada)
    saldos.append(saldo)


plt.plot(rodadas, saldos)
plt.show()
