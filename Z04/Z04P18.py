#Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
#wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
#podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
#maksymalnego podciągu

import random
N = 11

def podciag(tab):
    maxsum = 0

    for i in range(N):
        for a1 in range(0, N - 9):
            sumw = 0
            sumk = 0
            for an in range(a1, N):
                if an - a1 > 9:
                    break
                else:
                    sumw += tab[i][an]
                    sumk += tab[an][i]
                    maxsum = max(maxsum, max(sumw, sumk))
    return maxsum


def main():
    tab = [[random.randint(0, 1) for _ in range(N)] for _ in range(N)]
    print(podciag(tab))
    #for i in tab:
        #print(i)

main()