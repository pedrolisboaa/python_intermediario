"""
Funções Anônimas ou expressões lambdas
"""

soma = lambda x, y: x + y
print(soma(5, 5))

lista = [
    ['P1', 13],
    ['P2', 18],
    ['P3', 22],
    ['P4', 30],
    ['P5', 99.90],
    ['P6', 25.75]
]

lista.sort(key= lambda item: item[1])
print(lista)

lista.sort(key = lambda item: item[1], reverse=True)
print(lista)
