
import vendas.calc_preco
from vendas import calc_preco
from vendas.formata import preco

preco1 = 49.90
preco2 = 199.99
preco_com_aumento = calc_preco.aumento(preco1, 15, formata=True)
print(preco_com_aumento)

preco_com_aumento2 = calc_preco.aumento(preco2, 100, formata=True)
print(preco_com_aumento2)

preco_com_reducao = calc_preco.reducao(preco2, 50, formata=True)
print(preco_com_reducao)
