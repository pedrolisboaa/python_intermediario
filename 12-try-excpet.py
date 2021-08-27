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
  
  
print('----------')

def converte_numero(valor):
  try:
    valor = int(valor)
    return valor
  except ValueError:
    try: 
      valor = float(valor)
      return valor
    except ValueError:
      pass
  



numero = converte_numero(input('Digite um número: '))
if numero is not None:
  print(numero + 5)
else:
  print('Isso não é um número')

