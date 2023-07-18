pedido = int(input())
quantidade = int(input())
preco = 0

if pedido <= 0 or pedido > 10:
    print("pedido invalido")
elif quantidade < 1:
    print("quantidade invalida")
else:
    if pedido == 1:
        preco = 8.00
    elif pedido == 2:
        preco = 6.00
    elif pedido == 3:
        preco = 7.00
    elif pedido == 4:
        preco = 5.00
    elif pedido == 5:
        preco = 3.00
    elif pedido == 6:
        preco = 5.00
    elif pedido == 7:
        preco = 5.00
    elif pedido == 8:
        preco = 5.00
    elif pedido == 9:
        preco = 4.00
    elif pedido == 10:
        preco = 4.00

    conta = preco * quantidade
    print("R${:.2f}".format(conta))