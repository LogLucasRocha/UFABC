import pandas as pd
import numpy as np

df = pd.read_csv('https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download')
opcao = input('Deseja calcular média? Aperse s para sim e n para não: ')

if opcao == 's':
    df['Média'] = (df['Prova 1'] + df['Prova 2'] + df['Trabalho'])/3

print(df)