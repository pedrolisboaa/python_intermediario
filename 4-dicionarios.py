"""
Dicionário
"""
"""
d1 = {'chave': 'valor da chave'}
d1['nova chave'] = 'valor da nova chave'

print(d1['nova chave'])

d2 = dict(chave1='Valor da chave', chave2='Valor da outra chave')
print(d2)
"""
"""
d1 = {
    'str': 'Valor',
    123: 'Outro valor',
    (1, 2, 3, 4): 'Tupla'
}

print(d1[(1, 2, 3, 4)])
print(d1.get(123))

d1['chave_nao_existe'] = 'Pedro'

if d1.get('chave_nao_existe') is not None:
    print(d1.get('chave_nao_existe'))

d1.update({'Chave nova': 'Eai!'})
print(d1)

del d1['str']
print(d1)

print(123 in d1)
print(123 in d1.values())
print(123 in d1.keys())

print(len(d1))

"""
"""
dicionario = {
    'chave1': 'valor1',
    'chave2': 'valor2',
    'chave3': 'valor3',
    'chave4': 'valor4'
}

for k, v in dicionario.items():
    print(k, v)

"""
"""
clientes = {
    'cliente1': {
        'nome': 'Pedro',
        'sobrenome': 'Lisboa'
         },
    'cliente2': {
        'nome': 'Rosangela',
        'sobrenome': 'Lisboa'
    },
    'cliente3': {
        'nome': 'Barbara',
        'sobrenome': 'Silva'
    }
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(dados_k, dados_v)
"""

d1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd'}
c = d1.copy()
c[1] = 'Pedro'

print(d1)
print(c)


dic1 = {
    'a': 1,
    'b': 2,
    'c': 3
}

dic2 = {
    'e': 4,
    'd': 5,
    'f': 6
}

print(dic1)
print(dic2)

dic1.update(dic2)
print(dic1)