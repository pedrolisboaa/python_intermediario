"""
Escreva uma função para cada uma das quatro operações matemáticas simples:
"""


def adicao(x, y):
    return x + y


def subtracao(x, y):
    return x - y


def multiplicacao(x, y):
    return x * y


def divisao(x, y):
    if y != 0:
        return x / y
    return 'Não existe divisão por zero.'


print(adicao(5, 5))
print(subtracao(10, 2))
print(multiplicacao(2, 50))
print(divisao(10, 0))
print(divisao(5, 2))

