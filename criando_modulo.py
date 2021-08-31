"""
Criando nossos Módulos Python
"""
import math

PI = math.pi


def dobra_lista(lista):
    return [x * 2 for x in lista]


def multiplica_lista(lista):
    r = 1
    for i in lista:
        r *= i
    return r


if __name__ == '__main__':
    lista1 = [1, 2, 3, 4, 5]
    # print(dobra_lista(lista1))
    # print(multiplica_lista(lista1))
    # print(PI)



print(__name__)
