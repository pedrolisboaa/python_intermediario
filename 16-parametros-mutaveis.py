# Mutável: Listas, dicionários
# Imutável: Tuplas, strings, números, True, False, None

def lista_de_clientes(clientes_iteravel, lista=None):
    if lista is None:
        lista = []
    lista.extend(clientes_iteravel)
    return lista


clientes1 = lista_de_clientes(['Pedro', 'Juliana', 'Olívia'])
clientes2 = lista_de_clientes(('Rosa', 'Gabi', 'Marcelo'))

print(clientes1)
print(clientes2)