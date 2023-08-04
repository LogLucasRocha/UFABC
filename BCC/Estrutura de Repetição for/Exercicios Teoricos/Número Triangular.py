natural = int(input())

def numero_triangular(natural) -> bool:
    i = 1
    while (i * (i+1) * (i+2)) < natural:
        i += 1
    return (i * (i+1) * (i+2)) == natural

print(numero_triangular(natural))