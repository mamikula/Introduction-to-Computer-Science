#Napisać funkcję, która dla N-elementowej tablicy t wypełnionej liczbami
#naturalnym wyznacza długość najdłuższego, spójnego podciągu arytmetycznego.

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
        if t[i] - t[i - 1] == t[i - 1] - t[i - 2]:
            dl += 1
        else:
            if dl > maxdl:
                maxdl = dl
            dl = 1

    if dl > maxdl:
        maxdl = dl

    return maxdl

def main():
    t = [1, 3, 4 ,2 ,21 ,8 ,10, 20, 0, 1]
   # t = wypelnianie(t)

    print(t)
    print(ary(t))

main()