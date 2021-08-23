"""
O custo de um carro novo ao consumidor é obtido com a seguinte fórmula:
custo final = custo de fábrica +
              (custo de fábrica * percentual do distribuidor) +
              (custo de fábrica * percentual de impostos)
"""


def calcular_valor_total_carro(custoFabrica):
    custoDistribuidor = custoFabrica * 0.28
    custoImpostos = custoFabrica * 0.45
    return custoFabrica + custoDistribuidor + custoImpostos


print(calcular_valor_total_carro(10000))
