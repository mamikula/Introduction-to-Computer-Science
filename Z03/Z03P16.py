#Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą wartość typu bool
#oznaczającą, czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
#jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
#wartości).

import random
N = 10

def flg(t):
    for i in range(0, N):
        t[i] = random.randint(1, N)
    return t

def items(t):
    onemax = True
    onemin = True
    min = maks = t[0]

    for i in range(0, N):

        if t[i] == min:
            onemin = False

        if t[i] < min:
            min = t[i]
            onemin = True

        if t[i] == onemax:
            onemax = False

        if t[i] > maks:
            maks = t[i]
            onemax = True

    return onemin and onemax

t = [0] * N
t = flg(t)
print(t)
print(items(t))