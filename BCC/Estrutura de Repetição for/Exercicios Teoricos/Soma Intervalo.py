a = int(input('Insira o valor de a: '))
b = int(input('Insira o valor de b: '))
soma = 0

if a > b:
    print('a deve ser menor do que b')
else:
    for i in range(a, b+1):
        soma += i

print(soma)