def risco_doenca_cardiaca(idade: int, imc: float):
    if idade < 45:
        if imc < 22.0:
            print("Risco Baixo")
        elif imc >= 22.0:
            print("Risco Médio")
    if idade >= 45:
        if imc < 22.0:
            print("Risco Médio")
        elif imc >= 22.0:
            print("Risco Alto")

risco_doenca_cardiaca(49, 21)
