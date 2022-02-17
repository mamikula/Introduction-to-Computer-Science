#Dana jest tablica int t[MAX][MAX] wypełniona liczbami naturalnymi. Proszę napisać
#funkcję który odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda
#z liczb zawiera przynajmniej jedna cyfrę parzystą.
import random

def istnieje():
    N = 4
    t = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            t[i][j] = random.randint(11, 13)
            print(t[i][j], end=' ')
        print("\n")

    for w in range(N):
        niep = False
        for k in range(N):
            para = False
            liczba = t[w][k]
            while liczba > 0:
                if liczba % 2 == 0:
                    para = True
                    break
                else:
                    liczba //= 10

            if not para:
                niep = True
                break

        if not niep:
            print('Istnieje')
            return 0

    print('Nie istnieje')

    return 0

istnieje()