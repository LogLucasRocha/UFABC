populacao = int(input())
c_0 = int(input())
Tx_Contagio = float(input())
perc_imunidade = int(input())
novos_infectados = c_0
imunizados = c_0
dias = 0
imunizados_necessarios = populacao * (perc_imunidade / 100)

while imunizados < imunizados_necessarios:
    novos_infectados *= Tx_Contagio
    imunizados += novos_infectados
    dias += 1

print(dias)
