import random
import math
import functools 


media = lambda x: sum(x) / len(x)

def varianza(x):
    mu = media(x)
    acumulador = functools.reduce(lambda x: (x - mu)**2, x)
    return acumulador / len(x)

def desviacion_estandar(x):
    return math.sqrt(varianza(x))


if __name__ == '__main__':
    x = [random.randint(1, 31) for i in range(20)]
    mu = media(x)
    var = varianza(x)
    sigma = desviacion_estandar(x)

    