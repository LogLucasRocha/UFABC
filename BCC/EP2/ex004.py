import math

A = float(input())
B = float(input())
C = float(input())

if A >= B+C:
    print("NAO FORMA TRIANGULO")

elif A**2 == B**2 + C**2 or B**2 == A**2 + C**2 or C**2 == A**2 + B**2:
    print("TRIANGULO RETANGULO")

elif A**2 > B**2 + C**2 or B**2 > A**2 + C**2 or C**2 > B**2 + A**2:
    print("TRIANGULO OBTUSANGULO")

elif A**2 < B**2 + C**2 or B**2 < A**2 + C**2 or C**2 < B**2 + A**2:
    print("TRIANGULO ACUTANGULO")

if A == B != C or A == C != B or B == C != A:
    print("TRIANGULO ISOSCELES")

if A == B == C:
    print("TRIANGULO EQUILATERO")