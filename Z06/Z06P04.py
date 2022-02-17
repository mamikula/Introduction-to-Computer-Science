#Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
#wymiarach NxN ruchem skoczka szachowego.



def mozliwe(t, nw, nk):
    return nw >= 0 and nw < len(t) and nk >= 0 and nk < len(t) and t[nw][nk] == 0

def ruch(t, w, k, n, koniec, dw, dk):
    if koniec[0] == 1:
        return

    t[w][k] = n
    if n == len(t)**2:
        koniec[0] = 1 #oszukana referencja
        #for i in t:
            #print(i)


    else:
        for i in range(0, 8):
            nw = w + dw[i]
            nk = k + dk[i]
            if mozliwe(t, nw, nk):
                ruch(t, nw, nk, n + 1, koniec, dw, dk)

    #t[w][k] = 0


def main():
    dw = [-2, -1, 1, 2, 2, 1, -1, -2]
    dk = [1, 2, 2, 1, -1, -2, -2, -1]

    t = [[0 for _ in range(6)] for _ in range(6)]

    koniec = [0]
    ruch(t, 1, 1, 1, koniec, dw, dk)

main()