"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import zip_longest, count
### código

indice = count()

cidades = ['Brasília', 'São Paulo', 'Rio de Janeiro', 'Goiania', 'Palmas', 'Salvador']

estados = ['DF', 'SP', 'RJ', 'GO']

# zip = é um gerador
cidades_estados = zip(indice, estados, cidades)
cidades_estados_2 = zip_longest(indice, estados, cidades, fillvalue='BR')

# Forma não muito legal
#print(next(cidades_estados))
#print(next(cidades_estados))
#print(next(cidades_estados))
#print(next(cidades_estados))

print([c_e for c_e in cidades_estados])
#print([c_e for c_e in cidades_estados_2])
