import pandas as pd

df = pd.read_csv('https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download')

print(df)

if df['Prova 1'].median() < 50:
    df['Nova Prova 1'] = df['Prova 1'] + 10
else:
    df['Nova Prova 1'] = df['Prova 1']

print(df)

