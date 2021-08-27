"""
Combination, permutation e Product - itertools
Combinação - ordem não importa
Permutação - Ordem importa!
Ambos não repetem valores únicos
Produto - Ordem importa e repete valores únicos
"""
from itertools import combinations, permutations, product

pessoas = ['Luiz', 'Andre', 'Eduardo', 'Letícia', 'Olívia', 'Marcelo', 'Rosangela']

quantidade_de_combinacoes = 0
for grupo in product(pessoas, repeat=2):
    quantidade_de_combinacoes += 1
    print(grupo)

print(quantidade_de_combinacoes)
print(bytes(grupo))
