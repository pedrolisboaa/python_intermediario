"""
Funções 2
"""


def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2
    else:
        return 'Conta inválida.'


divide = divisao(10, 0)
print(divide)
