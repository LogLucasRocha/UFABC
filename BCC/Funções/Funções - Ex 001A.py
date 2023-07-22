def lucro(nc):
    L = (50 * nc) - (48 * (nc) ** 0.9) - 50
    print("R$ {:.2f}".format(L))

lucro(1)
lucro(4)
lucro(10)


