#Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami naturalnym
#wyznacza długość najdłuższego, spójnego podciągu geometrycznego.

#nie moze byc zera bo naturalne 8)

import random
N = 10

def wypelnianie(t):
    for i in range(0, N):
        t[i] = random.randint(1, N)
    return t


def ary(t):
    dl = 2
    maxdl = 2
    for i in range(2, N):
        if t[i] / t[i - 1] == t[i - 1] / t[i - 2]:
            dl += 1
        else:
            if dl > maxdl:
                maxdl = dl
            dl = 1

    if dl > maxdl:
        maxdl = dl

    return maxdl

def main():
    #t = [1, 2, 4, 8, 16, 32, 6, 12, 24, 10]
    t = [0]*N
    t = wypelnianie(t)

    print(t)
    print(ary(t))

main()