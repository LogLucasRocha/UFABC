N = int(input())


def imprimir_com_pim(N):
    num = 1
    count_pim = 0

    while count_pim != N:
        if num % 4 == 0:
            print("PIM")
            count_pim += 1
        else:
            print(num, end=" ")
        num += 1


imprimir_com_pim(N)
