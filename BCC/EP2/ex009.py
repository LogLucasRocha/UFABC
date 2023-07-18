aspecto = str(input())

if aspecto == "Sol":
    umidade = str(input())
    if umidade == "Elevada":
        print("N")
    elif umidade == "Normal":
        print("S")

elif aspecto == "Nuvens":
    print("S")

elif aspecto == "Chuva":
    umidade = str(input())
    vento = str(input())
    if umidade == "Elevada" and vento == "Fraco":
        print("S")
    elif umidade == "Normal" and vento == "Fraco":
        print("S")
    else:
        print("N")