# listas, tuplas, str -> Sequencias -> Iteraveis

nome = 'Pedro Henrique'
iterador = iter(nome)
gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('-------------')
for letra in gerador:
  print(letra)
