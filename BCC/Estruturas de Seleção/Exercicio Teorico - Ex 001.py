def maior(a, b, c):
    if (a > b) and (a > c):
        print("{} é maior do que {} e {}.".format(a, b, c))
    elif (b > a) and (b > c):
        print("{} é maior do que {} e {}.".format(b, a, c))
    elif (c > a) and (c > b):
        print("{} é maior do que {} e {}.".format(c, a, b))

maior(7, 20, 3)