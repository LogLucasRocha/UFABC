N1 = float(input("Digite a nota 1: "))
N2 = float(input("Digite a nota 2: "))
Media = (N1 + N2) / 2


def media():
    if (N1 > 10 or N1 < 0) or (N2 > 10 or N2 < 0):
        print("Nota Invalida!")
    elif Media > 6:
        print("Média = {}".format(Media))
        print("Aprovado")
    else:
        print("Média = {}".format(Media))

    if Media < 6:
        REC = input("Deseja fazer REC? (S/N): ")
        if REC == "S":
            NREC = float(input("Digite a nota da REC: "))
            Media_Rec = (Media + NREC) / 2
            print("Média após REC = {}".format(Media_Rec))
            if Media_Rec >= 5:
                print("Aprovado")
            else:
                print("Reprovado")
        elif REC == "N":
            if Media >= 5:
                print("Aprovado")
            else:
                print("Reprovado")


media()
