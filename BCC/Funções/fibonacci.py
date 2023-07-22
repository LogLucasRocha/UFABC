import math

def ionesimo (i):
    return round(((((1 + 5 ** (1/2)) / 2) ** i) - (((1 - 5 ** (1/2)) / 2) ** i)) / 5 ** (1/2))
print (ionesimo(10))