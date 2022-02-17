#Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
#wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
#elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
#wartość sumy, funkcja powinna zwrócić wartość typu bool.

from random import randint

N = 3

def fun(t, w, k, n ,sum):
    if sum == 0 and n > 0:
        return True

    elif n == N: return False
    elif sum < 0: return False

    for i in range(N):
        for j in range(N):
            #print(i, j)
            if w[i] == False and k[j] == False:
                w[i] = True
                k[j] = True
                if fun(t, w, k, n + 1, sum - t[i][j]):
                    return True
                w[i] = False
                k[j] = False

    return False

def istnieje(t, sum):

    w = [False]*N
    k = [False]*N
    return fun(t, w, k, 0, sum)


def main():
    t = [[randint(1, 1) for _ in range(N)] for _ in range(N)]
    for i in t:
        print(i)

    print(istnieje(t, 10))

main()
