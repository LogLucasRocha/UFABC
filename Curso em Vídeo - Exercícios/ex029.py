velocidade = float(input("Digite a velocidade do veículo em km/h: "))
if velocidade > 80:
    multa = 7 * (velocidade - 80)
    print("você foi multado em R${:.2f}!".format(multa))

