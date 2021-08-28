def retornar_calculo(n):
    import math
    if n > 0:
        return math.sqrt(n)
    return math.pow(n, 2)


calculo1 = retornar_calculo(9)
calculo2 = retornar_calculo(-9)

print(calculo1)
print(calculo2)