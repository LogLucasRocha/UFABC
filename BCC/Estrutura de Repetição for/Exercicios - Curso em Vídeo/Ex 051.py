primeiro_termo = int(input())
razao = int(input())
n = 10
an = primeiro_termo + (n-1) * razao

for pa in range(primeiro_termo, an + 1, razao):
    print(pa)