#Proszę napisać program, który wypełnia tablicę int tab[MAX] liczbami pseudolosowymi
#z zakresu [1 .. 1000], a następnie wyznacza i wypisuje sumę 10 największych elementów
#z tablicy

import random

M = 15

def numbers():
    tab = [random.randint(1, 15) for i in range(M)]

    top = [0]*10

    for z in range(M):
        print(tab[z])
        if tab[z] < top[9]:
            continue

        for i in range(10):

            if tab[z] > top[i]:
                for j in range(9, i, -1):
                    top[j] = top[j - 1]

                top[i] = tab[z]
                break

    suma = 0
    for i in range(10):
        suma += top[i]

    print(top, suma)
    return(suma)


numbers()