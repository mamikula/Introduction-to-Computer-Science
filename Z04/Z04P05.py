#Dana jest tablica T[N][N] wypełniona liczbami CALKOWITYMI. Proszę napisać funkcję, która
#zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
#element do sumy elementów wiersza w którym leży element jest największa.
import random


def maxil():

    N = 4
    t = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            t[i][j] = random.randint(0,0)
            print(t[i][j], end='     ')
        print("\n")

        minw = 10000000000000000000
        maxk = 0
        iw = 0
        ik = 0
    for i in range(N):
        sumk = 0
        sumw = 0
        for j in range(N):
            sumk += t[j][i]
            sumw += t[i][j]
        if sumk > maxk:
            maxk = sumk
            ik = i
        if sumw < minw:
            minw = sumw
            iw = i

    if minw == 0:
        print(iw, ik, minw, maxk, 'nie mozna dzielic przez 0')
    else:
        print(iw, ik, minw, maxk, maxk / minw)
    return 0
maxil()