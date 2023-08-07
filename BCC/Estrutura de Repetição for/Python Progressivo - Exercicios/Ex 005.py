populacao_A = int(input())
taxa_crescimento_A = float(input())
populacao_B = int(input())
taxa_crescimento_B = float(input())
contador = 0

while populacao_A <= populacao_B:
    populacao_A *= taxa_crescimento_A
    populacao_B *= taxa_crescimento_B
    contador += 1

print(contador)