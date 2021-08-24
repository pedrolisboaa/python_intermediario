"""

def funcao(*args, **kwargs):
    print(args)
   
    idade = kwargs.get('idade')
    if idade == None:
        print('Não foi passada idade')
    else:
        print(idade)

    nome = kwargs.get('nome')
    if nome != None:
        print(f'Olá {nome.upper()}')
    else:
        print('Nome não encontrado.')


lista_1 = [1, 2, 3, 4, 5]
lista_2 = [10, 20, 30, 40, 50]

funcao(*lista_1, *lista_2, nome='Pedro', idade="28")
