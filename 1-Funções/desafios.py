"""
Desafios
"""


def imprimi_saudacao(nome, saudacao):
    return f'{saudacao.capitalize()} {nome.capitalize()}, seja bem vindo!'


def soma_todos(numero_1=0, numero_2=0, numero_3=0):
    return numero_1 + numero_2 + numero_3


def mais_percentual(numero, percentual):
    total = numero + (numero * percentual / 100)
    return total


def buzz_fizz(numero):
    if numero % 2 == 0:
        return f'Fizz - O número foi {numero}'
    if numero % 3 == 0 and numero % 5 == 0:
        return f'FizzBuzz - O número foi {numero}'
    if numero % 5 == 0:
        return f'Buzz - O número foi {numero}'
    return f'{numero} - O número foi {numero}'


import random

# print(imprimi_saudacao('pedro', 'boa tarde'))
# conta = soma_todos(5, 7, 9)
# print(conta)
# print(mais_percentual(1000, 50))
# print(buzz_fizz(2))
# print(buzz_fizz(5))
# print(buzz_fizz(7))
#
# print(buzz_fizz(random.randint(0, 1000)))

numero = random.randint(0, 100000000)
contador = 0
maior_numero = []

while numero != 666:
    print(buzz_fizz(numero))
    numero = random.randint(0, 100000)
    maior_numero.append(numero)
    contador += 1

print(f'Foram repetidas {contador}x até achar o 666')
print(f'O maior número foi o {max(maior_numero)}')
