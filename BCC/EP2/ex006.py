import math
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
eficiencia = float(input())
litros = float(input())
distancia = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
consumo = distancia / eficiencia
if litros >= consumo:
    print("S")
else:
    print("N")