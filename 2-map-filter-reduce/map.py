from dados import pessoas, produtos, lista


# nova_lista_dobro = map(lambda x: x * 2, lista)
# nova_lista_quadrado = map(lambda x: x ** 2, lista)
# print(list(nova_lista_dobro))
# print(list(nova_lista_quadrado))
#
# nova_lista_dobro_2 = [x * 2 for x in lista]
# nova_lista_quadrado_2 = [x ** 2 for x in lista]
# print(nova_lista_dobro_2)
# print(nova_lista_quadrado_2)


def aumenta_preco(p):
    p['preco'] = round(p['preco'] * 1.05, 2)
    return p


#            primeira expressão sempre é uma função
# precos = map(aumenta_preco, produtos)
#
# for preco in precos:
#     print(preco)

nomes = map(lambda n: n['nome'], pessoas)
print(list(nomes))
