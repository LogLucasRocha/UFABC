populacao_A = 80000
taxa_crescimento_A = 1.03
populacao_B = 200000
taxa_crescimento_B = 1.015
contador = 0

while populacao_A <= populacao_B:
    populacao_A *= taxa_crescimento_A
    populacao_B *= taxa_crescimento_B
    contador += 1

print(contador)
