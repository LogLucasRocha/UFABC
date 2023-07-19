# Exemplo de definição de uma função
def mensagem(msg):
    print("-" * 30)
    print(msg)
    print("-" * 30)


def soma(a, b):
    s = a + b
    print(s)


def dobra(a, b):
    a_dobrado = a * 2
    b_dobrado = b * 2
    print(a_dobrado, b_dobrado)


mensagem("Programa Inicializado")

soma(1, 2)
dobra(1, 2)

mensagem("Programa Finalizado")
