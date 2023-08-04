natural = int(input())


def potencia(natural):
    i = 0
    while (2 ** i) <= natural:
        print(2 ** i)
        i += 1


potencia(natural)
