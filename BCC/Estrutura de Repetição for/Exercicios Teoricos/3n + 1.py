x = int(input())
contador = 0


while x > 1:
    if x % 2 == 0:
        x /= 2
    elif x % 2 == 1:
        x = (x * 3) + 1
    contador += 1

print(contador+1)