import math


# Aproximação de Schneider

def pi1():
    pi = math.sqrt(7 + math.sqrt(6 + math.sqrt(5)))
    print(pi)


# Aproximação de S. Irvine

def pi2():
    pi = math.sqrt(math.sqrt((3 ** 4) + ((19 ** 2) / 22)))
    print(pi)


pi1()
pi2()
