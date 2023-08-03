def main():
    N = int(input())
    R = [int(input()) for _ in range(N)]
    queda = 0
    for i in range(N - 1):
        if R[i] > R[i + 1]:
            queda = i + 2
            break
    print(queda)

if __name__ == "__main__":
    main()