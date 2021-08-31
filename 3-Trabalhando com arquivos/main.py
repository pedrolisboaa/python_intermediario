"""
Trabalhando com arquivos:
    Criando
    Lendo
    Escrevendo
    Apagando
"""


"""
Forma mais básica de criar um arquivo em PYTHON
file = open('abc.txt', 'w+')
file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')

file.seek(0, 0)
print('Lendo Arquivo')
print(file.read())
print('###############')

file.seek(0, 0)
print(file.readline(), end="")
print(file.readline(), end="")
print(file.readline(), end="")
print("###############")

file.seek(0, 0)
for linha in file.readlines():
    print(linha, end="")

file.close()
"""

# file = open('teste.txt', 'w+')
# file.write('Pedro Lisboa\n')
# file.write('Deu certo')
#
# file.seek(0, 0)
# print(file.read())
# file.close()
"""
Outra forma de abrir arquivo
try:
    file = open('arquivoTry', 'w+')
    file.write('Linha')
    file.seek(0, 0)
    print(file.read())
finally:
    file.close()
"""

# Forma pythonica

# Escrevendo
# with open('novo_teste.txt', 'w+') as file:
#     file.write('Pedro Lisboa\n')
#     file.write('Juliana Oliveira\n')
#     file.write('Olívia Oliveira\n')
#
#     file.seek(0, 0)
#     print(file.read())

"""
# Somente leitura
with open('novo_teste.txt', 'r') as file:
    print(file.read())


# Escrevendo
with open ('novo_teste.txt', 'a+') as file:
    file.write('Banana\n')
    file.write('Maçã\n')


print('----------')
with open ('novo_teste.txt','r') as file:
    print(file.read())"""

# Removendo
# import os
# os.remove('arquivoTry')

import json

d1 = {
    'Pessoa1': {
        'nome': 'Pedro',
        'idade': 28,
        'sexo': 'm'
    },
    'Pessoa2': {
        'nome': 'Juliana',
        'idade': 25,
        'sexo': 'f'
    },
    'Pessoa3': {
        'nome': 'Olivia',
        'idade': 1,
        'sexo': 'f'
    }
}

d1_json = json.dumps(d1, indent=True)
print(d1_json)

with open('json.txt', 'w+') as file:
    file.write(d1_json)

    file.seek(0, 0)
    print(file.read())
