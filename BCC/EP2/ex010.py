hi = int(input())
mi = int(input())
hf = int(input())
mf = int(input())

dh = hf - hi
dm = mf - mi

if dh < 0 or (dh == 0 and dm < 0):
    duracao_horas += 24

if  dm < 0:
    dm += 60
    dh -= 1

if hi == hf and mi == mf:
    duracao_horas = 24

print(f"Duração do jogo: {dh}h{dm}m")