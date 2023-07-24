def maior(a, b, c, d):
    if (a > b) and (a > c) and (a > d):
        print("{} é maior do que {}, {} e {}.".format(a, b, c, d))
    elif (b > a) and (b > c) and (b > d):
        print("{} é maior do que {}, {} e {}.".format(b, a, c, d))
    elif (c > a) and (c > b) and (c > d):
        print("{} é maior do que {} e {}.".format(c, a, b, d))
    elif (d > a) and (d > b) and (d > c):
        print("{} é maior do que {} e {}.".format(d, a, b, c))

maior(7, 20, 3, 29)