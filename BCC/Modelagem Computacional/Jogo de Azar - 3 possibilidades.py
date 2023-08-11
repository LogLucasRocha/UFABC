import random as rd
import matplotlib.pyplot as plt

entrada = 1
saldo = 100
rodada = 0
faliu = 0
prosperou = 0

for i in range(0,1000):
  saldo = 100
  aposta = 20
  while saldo > 0 and saldo < 200:
    sorteio = rd.randint(1,3)  # sorteio entre 1, 2 e 3, com a mesma probabilidade de cada um
    if sorteio == 1:
      saldo = saldo+aposta
    else:
      saldo = saldo-aposta
  if saldo<=0:
    faliu = faliu+1
  else:
    prosperou = prosperou+1

print("O jogador faliu",faliu,"vezes")
print("O jogador prosperou",prosperou,"vezes")