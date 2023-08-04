x = int(input())
contador = 0


while x > 1:
    if x % 2 == 0:
        x /= 2
        print(x)
    elif x % 2 == 1:
        x = (x * 3) + 1
        print(x)
    contador += 1

print(f'O número de passos até o fim do programa foi {contador + 1}')