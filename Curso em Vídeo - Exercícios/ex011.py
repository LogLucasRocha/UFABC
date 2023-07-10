l = float(input("Largura em metros quadrados: "))
h = float(input("Altura em metros quadrados: "))
area = l * h
litros_de_tinta = area / 2
print("A quantidade de tinta necessária para pintar essa parede de {} metros quadrados é {} litros.".format(area, litros_de_tinta))