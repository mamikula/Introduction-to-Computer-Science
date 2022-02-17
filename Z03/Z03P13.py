#Proszę napisać program, który wypełnia N-elementową tablicę t liczbami
#pseudolosowymi, a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego
#znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu. Na przykład dla tablicy:
# t=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15] odpowiedzią jest liczba 4.

N = 15

def max_len(t):
    for i in range(N - 1, 0, -1):
        for j in range(0, N - i):
            if rev(j, j + i - 1, t):
                print("\n", i)
                return i + 1
    print(0)
    return 0

def rev(idp, idk, t):

    dl = idk - idp + 1
    for i in range(0, N):
        if t[i] == t[idk]:
            k = idk - 1
            p = i + 1
            count = 1
            while k >= idp:
                if t[p] == t[k]:
                    p += 1
                    k -= 1
                    count += 1

                else:
                    count = 0
                    p = 0
                    k = 0

                if count == dl:
                    if count < 2:
                        return False
                    for w in range(i, i + dl):
                        print(t[w], end=",")
                    return True

    return False





#t = [2, 9, 3, 1, 7, 11, 9, 6, 7, 7, 1, 3, 9, 12, 15]
t = [0]*N
max_len(t)
