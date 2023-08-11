import pandas as pd

df = pd.read_csv('https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download')

print(df)

coluna = str(input('Digite a coluna a ser selecionada (Prova 1, Prova 2, Trabalho): '))

opcao = str(input('Digite uma das opções (Var, DP ou amplitude): '))

if opcao == 'Var':
    variancia = df[coluna].var()
    variancia = variancia.round(2)
    print(variancia)

elif opcao == 'DP':
    dp = df[coluna].std()
    dp = dp.round(2)
    print(dp)

elif opcao == 'amplitude':
    ampl = df[coluna].max() - df[coluna].min()
    ampl = ampl.round(2)
    print(ampl)

else:
    print('Erro de entrada.')