#Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym wyznacza
#długość najdłuższego, spójnego podciągu rosnącego.

N = 10

import random

def podciag(tab):
    dlugosc = 1
    maxdl = 1
    for i in range(1, N):
        if tab[i - 1] < tab[i]:
            dlugosc += 1
        else:
            if dlugosc > maxdl:
                maxdl = dlugosc
            dlugosc = 1

    if dlugosc > maxdl:
        maxdl = dlugosc

    return maxdl

def main():
    #tab = [1, 1, 1, 1, 1, 2, 3, 4, 5, 6]
    tab = [0] * N
    for i in range(0, N):
        tab[i] = random.randint(1, N)
    print(tab)
    print(podciag(tab))

main()