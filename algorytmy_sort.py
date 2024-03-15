import threading
import sys

sys.setrecursionlimit(2100000000)
threading.stack_size(2000000)

# -------------------------------------------------------------------------------------------------------------------
def bubble_sort(lista):
    global zamiany, porownania
    for i in range(len(lista) - 1):
        swapped = False
        for j in range(len(lista) - i - 1):
            porownania += 1
            if lista[j] < lista[j + 1]:
                zamiany += 1
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                swapped = True
        if swapped == False:
            break
    return lista


# -------------------------------------------------------------------------------------------------------------------
def selection_sort(lista):
    global zamiany, porownania
    for i in range(len(lista)):
        minimum = i
        for j in range(i + 1, len(lista)):
            porownania += 1
            if lista[minimum] < lista[j]:
                minimum = j
        zamiany += 1
        lista[minimum], lista[i] = lista[i], lista[minimum]
    return lista


# -------------------------------------------------------------------------------------------------------------------
def insertion_sort(lista):
    global zamiany, porownania
    for i in range(1, len(lista)):
        key = lista[i]
        j = i - 1
        while j >= 0 and key > lista[j]:
            porownania += 1
            zamiany += 1
            lista[j + 1] = lista[j]
            j = j - 1
        zamiany += 1
        lista[j + 1] = key
    return lista


# -------------------------------------------------------------------------------------------------------------------
def merge_sort(lista):
    global zamiany, porownania
    if len(lista) > 1:
        mid = len(lista) // 2
        L = lista[:mid]
        P = lista[mid:]

        merge_sort(L)
        merge_sort(P)
        i = j = k = 0

        while i < len(L) and j < len(P):
            porownania += 1
            if L[i] >= P[j]:
                zamiany += 1
                lista[k] = L[i]
                i += 1
            else:
                zamiany += 1
                lista[k] = P[j]
                j += 1
            k += 1

        while i < len(L):
            zamiany += 1
            lista[k] = L[i]
            i += 1
            k += 1

        while j < len(P):
            zamiany += 1
            lista[k] = P[j]
            j += 1
            k += 1
    return lista


# -------------------------------------------------------------------------------------------------------------------
def partition(lista, low, high):
    global zamiany, porownania
    pivot = lista[high]
    i = low - 1

    for j in range(low, high):
        porownania += 1
        if lista[j] >= pivot:
            i = i + 1
            zamiany += 1
            (lista[i], lista[j]) = (lista[j], lista[i])

    zamiany += 1
    (lista[i + 1], lista[high]) = (lista[high], lista[i + 1])
    return i + 1


def quick_sort(lista, low, high):
    global zamiany, porownania, recursion
    recursion += 1
    if low < high:
        pi = partition(lista, low, high)
        if recursion%1000 == 0:
            thread1 = threading.Thread(target=quick_sort, args=(lista, low, pi - 1))
            thread1.start()
            thread1.join()
        else:
            quick_sort(lista, low, pi - 1)
        if recursion%1000 == 0:
            thread2 = threading.Thread(target=quick_sort, args=(lista, pi + 1, high))
            thread2.start()
            thread2.join()
        else:
            quick_sort(lista, pi + 1, high)
    return lista


# -------------------------------------------------------------------------------------------------------------------
def heapify(lista, size, i):
    global zamiany, porownania
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    porownania += 1
    if l < size and lista[l] < lista[smallest]:
        zamiany += 1
        smallest = l

    porownania += 1
    if r < size and lista[r] < lista[smallest]:
        zamiany += 1
        smallest = r

    porownania += 1
    if smallest != i:
        zamiany += 1
        lista[i], lista[smallest] = lista[smallest], lista[i]
        heapify(lista, size, smallest)


def heap_sort(lista):
    global zamiany, porownania
    size = len(lista)

    for i in range(size // 2, -1, -1):
        heapify(lista, size, i)

    for i in range(size - 1, -1, -1):
        zamiany += 1
        lista[i], lista[0] = lista[0], lista[i]
        heapify(lista, i, 0)
    return lista

