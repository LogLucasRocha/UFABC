quantidade_pessoas = int(input())
contador_idade = 0
soma_idade = 0
contador_maioridade = 0

while contador_idade < quantidade_pessoas:
    idade = int(input())
    if idade >= 18:
        contador_maioridade += 1
    soma_idade += idade
    contador_idade += 1


porcentagem_maioridade = (contador_maioridade / quantidade_pessoas) * 100
media_idade = (soma_idade / quantidade_pessoas)

print(f'{round(porcentagem_maioridade, 1)}%')
print("{:.1f}".format(media_idade))
