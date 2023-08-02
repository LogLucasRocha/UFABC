N = int(input())

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_fatorial(n - 1)

def efatorial(numero):
    x = 0
    while True:
        fatorial_x = calcular_fatorial(x)
        if fatorial_x == numero:
            return True
        elif fatorial_x > numero:
            return False
        x += 1


if efatorial(N):
    print("Verdadeiro")
else:
    print("Falso")