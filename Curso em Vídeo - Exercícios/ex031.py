distancia = float(input("Digite a distância de sua viagem em KM: "))
if  distancia <= 200:
    valor = 0.5 * distancia
    print("O preço de sua viagem é de R${:.2f}".format(valor))
elif distancia > 200:
    valor = (200*0.5) + ((distancia - 200) * 0.45)
    print("O preço de sua viagem é de R${:.2f}".format(valor))