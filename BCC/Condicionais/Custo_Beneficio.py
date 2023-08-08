preco_5kg = float(input())
preco_3kg = float(input())

razao_5kg = preco_5kg / 5
razao_3kg = preco_3kg / 3

if razao_3kg < razao_5kg:
    print('O pacote com maior custo benefício é o de 3 kg.')
else:
    print('O pacote com maior custo benefício é o de 5 kg.')

