import sys
import time


def gera():
    for i in range(100):
        yield i
        time.sleep(0.1)


def gera2():
    variavel = 'valor 1'
    yield variavel
    variavel = 'valor 2'
    yield variavel
    variavel = 'valor 3'
    yield variavel


# g = gera()
# for v in g:
#     print(v)

g2 = gera2()
print(next(g2))
print(next(g2))
print(next(g2))

# outra forma de criar gerador

l1 = [x for x in range(100)]
print(type(l1))
print(l1)
l2 = (x for x in range(100))
print(type(l2))
print(l2)
