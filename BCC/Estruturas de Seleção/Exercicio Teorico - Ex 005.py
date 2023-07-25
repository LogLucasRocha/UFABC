tipo = input("Tipo (AMPM ou 24H): ")
horas = int(input())
minutos = int(input())

def horario():
    if tipo == "AMPM":
        print("Horas: {}".format(horas))
        print("Minutos: {}".format(minutos))
        if (horas > 12) or (horas < 0):
            print("Hora invalida!")
        else:
            print("Hora valida!")
    if tipo == "24H":
        print("Horas: {}".format(horas))
        print("Minutos: {}".format(minutos))
        if (horas > 24) or (horas < 0):
            print("Hora invalida!")
        else:
            print("Hora valida!")
horario()