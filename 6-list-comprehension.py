"""
List Comprehension em Python
"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel for variavel in l1]
l3 = [variavel * 2 for variavel in l1 ]

exemplo1 = [(v, v2) for v in l1 for v2 in range(2)]

lista_nomes = ['Pedro', 'Juliana', 'Olívia', 'Marcelo']
lista_nomes_trocados = [nome.replace('a', '@') for nome in lista_nomes]
lista_nomes_upper = [nome.upper() for nome in lista_nomes]

print(l2)
print(l3)
print(exemplo1)
print(lista_nomes_trocados)
print(lista_nomes_upper)


lista_0_100 = list(range(100))
lista_pares_0_100 = [numero for numero in lista_0_100 if numero % 2 == 0]
lista_3_7 = [n for n in lista_0_100 if n % 3 == 0 if n % 7 == 0]
print(lista_pares_0_100)
print(lista_3_7)

lista_nao_e = [v if v % 3 == 0 else 'Não é' for v in lista_0_100]
print(lista_nao_e)
