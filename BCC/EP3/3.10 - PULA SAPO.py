def entrada():
    p = int(input())
    n = int(input())
    x = []
    for i in range(n):
        x.append(int(input()))
    return p, n, x


def verificacao(a, b, p):
    return abs(a - b) > p


def main():
    p, n, x = entrada()
    for i in range(n - 1):
        if verificacao(x[i], x[i + 1], p):
            print('GAME OVER')
            return

    print('YOU WIN')


main()
