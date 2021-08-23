"""
Faça uma função para calcular o dobro de um número qualquer.
"""


def mostra_o_dobro(numero):
    if type(numero) == str:
        return 'Error'
    return numero * 2


print(mostra_o_dobro('p'))
print(mostra_o_dobro(2))