import math

a = int(input())
a_radians = math.radians(a)
sen = math.sin(a_radians)
cos = math.cos(a_radians)
tan = math.tan(a_radians)

print("O seno de {} graus é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.".format(a, sen, cos, tan))
