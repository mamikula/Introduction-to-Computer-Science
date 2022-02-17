#Proszę napisać program, który wypełnia tablicę int tab[MAX] trzycyfrowymi liczbami
#pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego
#znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu.
#Na przykład dla tablicy: 2,9,3,1,7,11,9,6,7,7,1,3,9,12,15 odpowiedzią jest liczba 4.
N = 15
from random import randint

def maxlen(t):
    for i in range(N - 1, 0, -1):
        for j in range(0, N - i):
            if rewers(j, j + i - 1, t):
                print('\n', i)
                return i + 1

    print(0)
    return 0

def rewers(idp, idk, t):
    ln = idk - idp + 1
    for i in range(N):
        if t[i] == t[idk]:
            p = i + 1
            k = idk - 1
            count = 1

            while k >= idp:
                if t[p] == t[k]:
                    count += 1
                    p += 1
                    k -= 1

                else:
                    count = 0
                    p = 0
                    k = 0

                if count == ln:
                    if count < 2:
                        return False
                    for w in range(i, i + ln):
                        print(t[w], end='')
                    return True

    return False



t = [2,9,3,1,7,7,9,8,7,7,1,3,9,12,15]
maxlen(t)