import pandas as pd

df = pd.read_csv("https://drive.google.com/u/1/uc?id=1ASOWhw5tp-kUbZcIlkg5eCKwZNJt6MwQ&export=download")
print(df) #imprimimos a tabela apenas para visulisar-la

indice_aluno = int(input("Digite o indice de aluno - numero inteiro de 0 a 99: ")) # lendo o indice de aluno, ou seja, numero da linha  (cada indice de aluno eh numero de uma linha da tabela)

prova1, prova2, trabalho = df[["Prova 1" , "Prova 2" , "Trabalho"]].loc[indice_aluno] # obtendo os valores (de Prova 1, Prova 2 e Trabalho) da linha ou seja indice_aluno lido
print("Notas sao: Prova1 = %.2f, Prova 2 = %.2f e Trabalho = %.2f"%(prova1,prova2,trabalho)) # imprimindo os valores obtidos

med = (prova1 + prova2 + trabalho)/3   # calculando a media aritmetica de notas
print("Media aritmetica = %.2f"%med)   # imprimindo a media aritmetica

# imprimindo o conceito dependendo de valor de media:
if med < 50:
  print("Conceito F")
elif med < 77:
  print("Conceito C ou D")
else:
  print("Conceito A ou B")