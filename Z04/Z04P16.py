#Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
#odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
#będących liczbami pierwszymi?

N = 3
import random

def pierwsze_cyferki(a):
    while a > 0:
            if a % 10 == 2 or a % 10 == 3 or a % 10 == 5 or a % 10 == 7:
                a //= 10
            else:
                return False
    return True

def cyferki(t):
    for i in range(N):
        czy = False
        for j in range(N):
            if pierwsze_cyferki(t[i][j]):
                czy = True
                break
        if not czy:
            return False
    return True

def main():
    tab = [[random.randint(23, 24) for _ in range(N)] for _ in range(N)]
    print(cyferki(tab))
    for i in tab:
        print(i)

main()