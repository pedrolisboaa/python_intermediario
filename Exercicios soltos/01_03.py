"""
Sabendo que a área quadrada é dada pela multiplicação dos lados, escreva um algoritmo que mostre a área
 quadrada de um espaço qualquer
"""


def area_do_quadrado(x, y):
    area = x * y
    return f'A área do quadrado é {area}m'


area1 = area_do_quadrado(5, 10)
print(area1)