"""
Count - Itertools
"""

from itertools import count

contador1 = count(start=5, step=0.5)

for valor in contador1:
  print(valor)

  if valor >= 10:
    break

contador2 = count(start=1)
alunos = ['Pedro', 'Juliana', 'Amanda', 'Marcia', 'Olivia']
alunos = list(zip(count(), alunos))
print(*alunos)
