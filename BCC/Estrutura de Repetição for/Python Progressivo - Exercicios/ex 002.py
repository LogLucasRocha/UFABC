nome = input().lower()
senha = input().lower()

while senha == nome:
    print(input('A senha não pode ser igual ao nome. Tente novamente.'))
print('Senha válida!')