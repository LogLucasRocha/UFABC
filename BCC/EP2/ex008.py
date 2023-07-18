x = float(input())
fx = 0

if x >= 2 and x < 3:
    fx = ((x - 1)**2) + 1

elif x >= 3 and x <= 7:
    fx = 1 - (x - 4)**2 - 2

elif x < 2 or x > 7:
    fx = 2

print("{:.4f}".format(fx))