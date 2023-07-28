N = int(input())
def imprimir_com_pim(N):
    for num in range(1, N + 1):
        if num % 4 == 0:
            print("PIM")
        else:
            print(num, end=" ")


imprimir_com_pim(N)