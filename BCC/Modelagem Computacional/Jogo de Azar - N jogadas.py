import random as rd
import matplotlib.pyplot as plt

entrada = 1
saldo = 100000
rodada = 0
rodadas = []
saldos = []


while rodada < 1001 and saldo > 0:
    numero_sorteado = rd.randint(1, 2)

    if numero_sorteado == entrada:
        print(f'Você acertou! O número sorteado foi {numero_sorteado}')
        saldo_atual = saldo + 20
        saldo = saldo_atual
        print(f'Saldo atual: R${saldo}')
    else:
        rodada += 1
        print(f'Você errou! O número sorteado foi {numero_sorteado}')
        saldo_atual = saldo - 20
        saldo = saldo_atual
        print(f'Saldo atual: R${saldo}')
        rodada += 1

    rodadas.append(rodada)
    saldos.append(saldo)


if saldo == 0:
    print('Você faliu!')


plt.plot(rodadas, saldos)
plt.xlabel('Rodadas')
plt.ylabel('Saldo')
plt.show()
