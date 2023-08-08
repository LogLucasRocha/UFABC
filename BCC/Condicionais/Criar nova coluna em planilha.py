import pandas as pd
import numpy as np

df = pd.read_csv('https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download')
opcao = input('Deseja calcular média? Aperse s para sim e n para não: ')

if opcao == 's':
    peso_1 = int(input('Digite o peso da prova 1: '))
    peso_2 = int(input('Digite o peso da prova 2: '))
    peso_trabalho = int(input('Digite o peso do trabalho: '))
    soma_pesos = peso_1 + peso_2 + peso_trabalho
    df['Média'] = ((df['Prova 1'] * peso_1) + (df['Prova 2'] * peso_2) + (df['Trabalho'] * peso_trabalho)) / soma_pesos

print(df)