natural = int(input())


def divisores(natural):
    d = 1
    while d <= natural:
        if natural % d == 0:
            print(d)
        d += 1


divisores(natural)
