"""
Desafio 2 Funções
"""

# Desafio Atividades - 1
def func_one(funcao):
    return funcao


def func_two():
    return 'Pedro Lisboa'


print(func_one(func_two()))


#Desafio 2

def funcao_um(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f'oi {nome}.'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}.'

executando = funcao_um(fala_oi, 'Pedro')
print(executando)
