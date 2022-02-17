#Dane są dwie tablice int t1[N], int t2[N] wypełnione liczbami naturalnymi. Proszę napisać funkcję, która
#sprawdza czy z każdej z tablic można wyciąć po jednym kawałku, tak aby suma elementów w obu kawałkach była:
#co najmniej drugą potęgą dowolnej liczby naturalnej. Łączna długości obu kawałków powinna wynosić 24.
N = 20
def potega(a):
    for i in range(2, a + 1):
        j = 2
        while i ** j <= a:
            if i ** j == a:
                return True
            j += 1

    return False

def kawalki(t1, t2):
    D = 24
    s1 = 0
    s2 = 0
    for l in range(1, min(N, D)):
        kaw = l
        if D - kaw < N:

            for i in range(0, N - kaw):
                for t in range(i, i + kaw):
                    s1 += t1[t]

                for j in range(0, N - kaw):

                    if j + D - kaw >= N:
                        break

                    for t in range(j, D - kaw + j):
                        s2 += t2[t]

                    if potega(s1 + s2):
                        return True
                    else:
                        s2 = 0

                s1 = 0

    return False



t1 = [2] * N
t2 = [3] * N

#print(potega(12))
print(kawalki(t1, t2))

#########3 nie działa