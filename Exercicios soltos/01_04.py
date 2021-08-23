"""
Exercício de lógica de programação para calcular o sucessor e o antecessor de um número qualquer.
"""


def antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1
    return f'antecessor = {antecessor}, numero = {numero}, sucessor = {sucessor}'


print(antecessor_e_sucessor(5))
