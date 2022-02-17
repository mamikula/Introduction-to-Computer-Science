#Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
#M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby
#naturalne. Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
#tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
#powinny zawierać zera.

# 1 2 4 6 6
# 2 3 5 6 7

import random
N = 2
M = N * N


def przepisz(tab1, tab2):

    tab2 = [0] * M
    tid = [0] * N #tablica indeksow
    przeniesione = 0

    while True:
        najmniejsza = False
        mini = 99999

        for i in range(N): #petla przechodzaca przez wszystkie wiersze tablicy
            if tid[i] == N: #z tego wiersza wybrane zostaly juz wszystkie elementy
                continue
            if tab1[i][tid[i]] < mini: #szukam najmnniejszego elementu
                minid = i
                mini = tab1[i][tid[i]]
                najmniejsza = True

        if not najmniejsza: #jezeli nie ma najmniejszej to znaczy ze wszystko juz zostalo przepisane
            print(tab2)
            return

        if przeniesione == 0: #do wpisania pierwszego elementu w t2
            tab2[0] = tab1[minid][0]
            tid[minid] += 1
            przeniesione += 1

        elif mini > tab2[przeniesione - 1]:
            tab2[przeniesione] = mini
            tid[minid] += 1
            przeniesione += 1

        else:
            tid[minid] += 1



def main():

    #t1 = [[0] * N for _ in range(N)]
    #t1 = [[1, 6, 11, 16, 21], [2, 10, 12, 17, 22], [3, 8, 13, 18, 23], [4, 9, 14, 19, 24], [5, 10, 15, 20, 25]]
    t2 = []

    t1 = [[random.randint(1, 2) for _ in range(N)] for _ in range(N)]
    #t1 = [[1, 3], [2, 4]]
    for i in t1:
        print(i)

    #print(t1)
    przepisz(t1, t2)



main()