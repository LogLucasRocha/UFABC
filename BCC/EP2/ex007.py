pedido = int(input())
quantidade = int(input())
if pedido <= 0 or pedido > 10:
    print("pedido invalido")
elif quantidade < 1:
    print("quantidade invalida")
