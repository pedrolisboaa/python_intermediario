"""
Funções - def em Python (Parte - 1)
"""


def saudacao(nome, idade):
    print(f'Olá {nome}, você tem {idade} anos?')


def soma(x=0, y=0):
    return f'{x + y}'


saudacao('pedro', 28)
print(soma(5))
print(soma(5, 8))
