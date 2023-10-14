import random
import collections

PALOS = ['espadas', 'corazones', 'rombos', 'treboles']
VALORES = ['as', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'sota', 'reina', 'rey']

def crear_baraja():
    """Crea una baraja con 52 cartas"""
    return [(palo, valor) for palo in PALOS for valor in VALORES]

def obtener_mano(barajas, tamano_mano):
    return random.sample(barajas, tamano_mano)

def main(tamano_mano, intentos):
    barajas = crear_baraja()

    manos = [obtener_mano(barajas, tamano_mano) for _ in range(intentos)]

    pares = 0

    for mano in manos:
        valores = list(map(lambda carta: carta[1], mano))
        contador = dict(collections.Counter(valores))

        if any(val == 2 for val in contador.values()):
            pares += 1

    probabilidad = pares / intentos

    print(probabilidad)


if __name__ == '__main__':
    tamano_mano = 5
    intentos = 10
    main(tamano_mano, intentos)