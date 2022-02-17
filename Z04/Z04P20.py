#Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
#Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
#przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
#wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi

N = 4
import random

def ileszachuje(t, w, k):
    sum = 0
    for i in range(N):
        sum += t[w][i]
        sum += t[i][k]

    sum -= 2 * t[w][k]
    return sum

def funkcja(tab):

    sum1 = -1
    sum2 = -1
    w1w = 0
    w1k = 0
    w2w = 0
    w2k = 0
    for i in range(N):
        for j in range(N):
            if ileszachuje(tab, i, j) > sum1:
                sum1 = ileszachuje(tab, i, j)
                w1w = i
                w1k = j
            elif ileszachuje(tab, i, j) > sum2:
                sum2 = ileszachuje(tab, i, j)
                w2w = i
                w2k = j

    print(w1w, w1k, w2w, w2k, sum1, sum2)
    return(w1w, w1k, w2w, w2k)

def main():
    tab = [[random.randint(1, 3) for _ in range(N)] for _ in range(N)]
    funkcja(tab)

    for i in tab:
        print(i)

main()