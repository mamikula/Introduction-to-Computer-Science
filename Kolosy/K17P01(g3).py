#Dwie liczby naturalne są „koleżankami” jeżeli mają przynajmniej dwie różne wspólne cyfry,
#np. 123 i 1345 lub 225 i 1235. Dana jest tablica t[N][N] wypełniona liczbami naturalnymi.
#Proszę napisać funkcję, która w tablicy t zeruje wszystkie liczby nie mające żadnej koleżanki.
#Do funkcji należy przekazać tablicę t. Funkcja powinna zwrócić ilość liczb naturalnych jaka
#pozostanie w tablicy
N = 10
from random import randint

def mo(w, k):
    if w >= 0 and w < N and k >= 0 and k < N:
        return True
    return False

def ko(a, b):
    la = [0] * N
    lb = [0] * N
    while a > 0:
        la[a % 10] += 1
        a //= 10
    while b > 0:
        lb[b % 10] += 1
        b //= 10
    l = 0
    for i in range(N):
        if la[i] != 0 and lb[i] != 0:
            l += 1
        if l == 2:
            return True
    return False

def wspolrzedne(t):
    cnt = 0
    for i in range(N):
        for j in range(N):
            jest = False

            if mo(i - 1, j - 1):
                if ko(t[i][j], t[i - 1][j - 1]):
                    jest = True
                    cnt += 1

            if mo(i - 1, j):
                if ko(t[i][j], t[i - 1][j]):
                    jest = True
                    cnt += 1

            if mo(i - 1, j + 1):
                if ko(t[i][j], t[i - 1][j + 1]):
                    jest = True
                    cnt += 1

            if mo(i, j - 1):
                if ko(t[i][j], t[i][j - 1]):
                    jest = True
                    cnt += 1

            if mo(i, j + 1):
                if ko(t[i][j], t[i][j + 1]):
                    jest = True
                    cnt += 1

            if mo(i + 1, j - 1):
                if ko(t[i][j], t[i + 1][j - 1]):
                    jest = True
                    cnt += 1

            if mo(i + 1, j):
                if ko(t[i][j], t[i + 1][j]):
                    jest = True
                    cnt += 1

            if mo(i + 1, j + 1):
                if ko(t[i][j], t[i + 1][j + 1]):
                    jest = True
                    cnt += 1

            if not jest:
                t[i][j] = 0
    return cnt

def main():
    t = [[randint(100, 999) for _ in range(N)] for _ in range(N)]
    wspolrzedne(t)
    for i in range(N):
        for j in range(N):
            print(t[i][j], end='     ')
        print('\n')

main()