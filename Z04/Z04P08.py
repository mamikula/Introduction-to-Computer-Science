#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
#co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
#się znaleźć taki ciąg oraz długość tego ciągu

#NIE DZIALA

N = 5
import random

def wypisz(t):
    for i in range(N):
        for j in range(N):
            print(t[i][j], end='    ')
        print("\n")

def podciag(tab):
    maxdl = 0
    k = N - 3
    for i in range(0, N - 3):
        dl1 = 2
        dl2 = 2
        for j in range(0, N - 3):

            if tab[j][j + i] // tab[j + 1][j + 1 + i] == tab[j + 1][j + 1 + i] // tab[j + 2][j + 2 + i]:
                dl1 += 1


            else:
                if dl1 > maxdl:
                    maxdl = dl1
                dl1 = 2

            if tab[k][k + i] // tab[k + 1][k + 1 + i] == tab[k + 1][k + 1 + i] // tab[k + 2][k + 2 + i]:# and k < N - 1:
                dl2 += 1

            else:
                if dl2 > maxdl:
                    maxdl = dl2
                dl2 = 2

        if dl1 > maxdl:
            maxdl = dl1
        if dl2 > maxdl:
            maxdl = dl2

        k -= 1

    if maxdl >= 3:
        print('Jest')
        return True

    else:
        print('Nie ma')
        return False

def main():

    #tab = [[0] * N for _ in range(N)]

    #for i in range(N):
        #for j in range(N):
            #tab[i][j] = random.randint(1, N)

    tab = [
        [1, 1, 1, 1, 1],
        [1, 2, 3, 4, 2],
        [2, 3, 6, 7, 3],
        [4, 1, 4, 3, 4],
        [1, 2, 3, 8, 9]
        ]

    wypisz(tab)
    podciag(tab)
main()