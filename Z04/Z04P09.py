#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która w
#poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
#narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
#czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu.

N = 15
import random

def kwadrat(t, il):
    pole = 0
    w = -1
    k = -1
    x = 0
    y = 3

    for bok in range(3, N, 2):
        x = 0
        y = 0
        while x + bok - 1 < N:

            while y + bok - 1 < N:
                #print(x, y, bok)

                if t[x][y] * t[x + bok - 1][y] * t[x + bok - 1][y + bok - 1] * t[x][y + bok - 1] == il:
                    w = x + (bok - 1) // 2
                    k = y + (bok - 1) // 2
                    print(w, k,  'Jest')
                    return(True, w, k, bok)

                #print(t[x][y], t[x + bok -1][y], t[x + bok - 1][y + bok - 1], t[x][y + bok - 1])
                x += 1
                y += 1
    print('Nie ma')
    return False

t = [[random.randint(1, 5) for _ in range(N)] for _ in range(N)]

kwadrat(t, 16)

for i in t:
    print(i)