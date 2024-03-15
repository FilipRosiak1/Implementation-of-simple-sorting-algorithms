import random
random.seed(213742069)


def lista_rosnaca(dlugosc):
    lista = random.sample(range(1, 10*dlugosc + 1), dlugosc)
    lista.sort()
    return lista


def lista_malejaca(dlugosc):
    lista = random.sample(range(1, 10*dlugosc + 1), dlugosc)
    lista.sort(reverse=True)
    return lista


def lista_rand(dlugosc):
    lista = random.sample(range(1, 10*dlugosc + 1), dlugosc)
    return lista


def lista_v(dlugosc):
    lista1 = list(range(dlugosc, 0, -2))
    lista2 = list(range(1 + dlugosc % 2, dlugosc + 1, 2))
    return lista1 + lista2


def lista_a(dlugosc):
    lista1 = list(range(dlugosc, 0, -2))
    lista2 = list(range(1 + dlugosc % 2, dlugosc + 1, 2))
    return lista2 + lista1

