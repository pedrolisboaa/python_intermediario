"""
Considerando todos meses como 30, faça uma função que calcule quantos meses tem em n dias.
"""


def calcula_meses(dias_totais):
    meses = dias_totais // 30
    dias = dias_totais % 30
    return f'{dias_totais} dias são {meses} meses e {dias} dias'



print(calcula_meses(700))