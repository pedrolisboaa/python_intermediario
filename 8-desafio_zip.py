"""
Somando duas listas e retornando uma lista com os valores somados.
"""

lista_a = [10, 2, 3, -4, 5, 6, 7]
lista_b = [1, 23.50, 31, 43.1]

lista_a_b = zip(lista_a, lista_b)

lista_soma = [valor_1 + valor_2 for valor_1, valor_2 in lista_a_b]
print(lista_soma)


#for valor_1, valor_2 in lista_a_b:
#  print(valor_1 + valor_2)
