salario = float(input("Digite o salário do funcionário: "))
aumento_percentual_absoluto = 15
indice = 1 + (15/100)
novo_salario =  salario * indice
novo_salario_f = "{:.2f}".format(novo_salario)

print("O novo salário do funcionário, com aumento de {}%, é de R${}".format(aumento_percentual_absoluto, novo_salario_f))