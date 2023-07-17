import random
ls = list(range(6))
random_num = random.choice(ls)
resposta = int(input("Digite um número: "))
if  resposta == random_num:
    print("Você acertou! O número sorteado foi {}.".format(random_num))
else:
    print("Você errou! O número sorteado foi {}.".format(random_num))