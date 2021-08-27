from dados import produtos, pessoas, lista

# com filter
novas_lista = filter(lambda x: x > 5, lista)
nova_lista_2 = filter(lambda x: x % 2 == 0, lista)
print(list(novas_lista))
print(list(nova_lista_2))

# com list compre...
nl = [x for x in lista if x > 5]
nl2 = [x for x in lista if x % 2 == 0]

print(nl)
print(nl2)


lista_produtos = filter(lambda p: p['preco'] > 10, produtos)

for produto in lista_produtos:
    print(produto)