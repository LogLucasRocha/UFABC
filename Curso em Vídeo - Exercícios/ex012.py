valor_do_produto = float(input("Digite o valor do produto: "))
desconto = 5
indice_de_desconto = (1 - (5/100))
novo_valor = (valor_do_produto * indice_de_desconto)
novo_valor_f = "{:.2f}".format(novo_valor)
print("O valor do produto com {} de desconto é R${}!".format(desconto,novo_valor_f))

