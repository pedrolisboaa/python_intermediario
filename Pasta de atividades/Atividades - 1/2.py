def calcula_raiz(numero):
    from math import sqrt
    try:
        numero = float(numero)
        if numero < 0:
            return 'Seu número deve ser positivo'
        return f'{sqrt(float(numero)):.2f}'
    except ValueError:
        return 'Você deve digitar um número válido'


numero = input('Digite um número para saber sua raiz: ')
print(calcula_raiz(numero))
