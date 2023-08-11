import pandas as pd

df = pd.read_csv('https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download')


entrada = str(input('Digite 1 para calcular a média simples e 2 para a média ponderer: '))

while entrada != '1' and entrada != '2':
    entrada = str(input('Insira um valor válido (1/2): '))


if entrada == '1':
    df['Média'] = (df['Prova 1'] + df['Prova 2'] + df['Trabalho']) / 3
    df['Média'] = df['Média'].round(2)
    print(df)
elif entrada == '2':
    peso_1 = int(input('Digite o peso da prova 1: '))
    peso_2 = int(input('Digite o peso da prova 2: '))
    peso_trabalho = int(input('Digite o peso do trabalho: '))
    soma_pesos = peso_1 + peso_2 + peso_trabalho
    df['Média'] = ((df['Prova 1'] * peso_1) + (df['Prova 2'] * peso_2) + (df['Trabalho'] * peso_trabalho)) / soma_pesos
    print(df)
