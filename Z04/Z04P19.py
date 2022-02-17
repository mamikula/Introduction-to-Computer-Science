#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka
#szachowego.
import random
N = 10

def mozliwe(i, j):
    if i < N and i >= 0 and j < N and j >= 0:
        return True
    return False


def konik(t, il):
    pary = 0
    for w in range(N):
        for k in range(N):
            if mozliwe(w + 1, k + 2) and t[w][k] * t[w + 1][k + 2] == il:
                pary += 1
            if mozliwe(w + 1, k - 2) and t[w][k] * t[w + 1][k - 2] == il:
                pary += 1
            if mozliwe(w + 2, k - 1) and t[w][k] * t[w + 2][k - 1] == il:
                pary += 1
            if mozliwe(w + 2, k + 1) and t[w][k] * t[w + 2][k + 1] == il:
                pary += 1
    return pary


def main():
    tab = [[random.randint(1, 20) for _ in range(N)] for _ in range(N)]
    print('pary =', konik(tab, 3))

    for i in tab:
        print(i)

main()

