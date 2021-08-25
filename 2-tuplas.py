"""
Tuplas - Python
"""

tupla_um = (1, 2, 3, 5, 6, 'Pedro', 'Maça')
tupla_dois = 1, 3, 5, 'Juliana', 'Melancia'
tupla_tres = tupla_um + tupla_dois

print(tupla_tres)

tupla_um = list(tupla_tres)
tupla_um[0] = 5000
print(tupla_um)
