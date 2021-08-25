"""
Os sets ou conjuntos

- add (adiciona),  update (atualiza), clear, discard
- union |
- intersection & (todos os elementos presentes nos dois sets)
- difference - (elementos apenas no set da esquerda)
- symmetric_difference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
set2 = set()
set2.add(1)
set2.add(2)
set2.update([5, 6, 8, 1, 2, 3])

print(set1)
print(set2)

set1.discard(10)
print(set1)

# removendo os elementos duplicados de uma lista  com set
lista = [1, 1, 1, 2, 2, 3, 3, 5, 6, 9, 8, 8, 8, 4, 5, 9, 2, 4, 'Pedro', 'Maçã', 'Pedro', 'Juliana', 'Juliana']
print(lista)

lista = set(lista)
print(lista)

s1 = {1, 2, 3, 4, 5}
s2 = {3, 4, 5, 6, 7}
s3 = s1 | s2
s4 = s1 & s2
s5 = s1 - s2
s6 = s1 ^ s2
print(s3)
print(s4)
print(s5)
print(s6)
