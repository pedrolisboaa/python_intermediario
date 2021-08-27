try:
  a = {}
  print(a)
except NameError as error:
  print(f'Erros do desenvolvedor')
except (IndexError, KeyError) as error:
  print(f'Existe um erro de indice')
except Exception as error:
  print(f'Ocorreu um erro inesperado')
else:
  print('Seu código foi executado com sucesso')
finally:
  print('Finalmente')

