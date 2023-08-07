nome = str(input('Digite o seu nome: '))
while len(nome) < 4:
    nome = input('O nome deve ter mais de 3 letras. Tente Novamente: ')
    break

idade = int(input('Digite a sua idade: '))
while (idade < 0) or (idade > 150):
    idade = input('Idade inválida. Tente novamente: ')
    break

salario = float(input('Digite o seu salário: '))
while salario <= 0:
    salario = float(input('O salário deve ser maior do que R$ 00.00. Tente novamente: '))
    break

sexo = str(input('Digite o seu sexo [M/F]: ')).lower()
while (sexo != 'f') and (sexo != 'm'):
    sexo = str(input('Sexo inválido. Digite M para masculino ou F para feminino: ')).lower()
    break

estado_civil = str(input('''Digite s para solteiro 
Digite c para casado 
Digite v para Viuvo 
Digite d para divorciado
''')).lower()
while (estado_civil != 'c') and (estado_civil != 's') and (estado_civil != 'v') and (estado_civil != 'd'):
    estado_civil = str(input('Digite um estado civíl válido: ')). lower()
    break
