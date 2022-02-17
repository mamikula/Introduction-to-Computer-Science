#Dana jest N-elementowa tablica t zawierająca liczby naturalne. W tablicy możemy przeskoczyć
#z pola o indeksie k o n pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby t[k]. Napisać funkcję
#sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.

# 1 nie jest liczba pierwsza wiec dla niej nie pa dzielnikow czyli nie ma przejscia dalej 

N = 6
import random

def skoki(tab):

    skok = [False] * N #tablica pól z ktorych mozna skakac dalej
    skok[0] = True

    for i in range(0, N):
        if skok[i]: #sprawdzenie czy z tego indeksu mozna isc dalej
            copy = tab[i]
            podzielnik = 2
            while copy > 1: #petla w ktorej beda "generowane wszystkie podzielniki czyli mozliwosci skoków
                if copy % podzielnik == 0:
                    if i + podzielnik < N:
                        skok[i + podzielnik] = True

                    if i + podzielnik == N - 1:
                        return True

                    while copy % podzielnik == 0:
                        copy //= podzielnik

                podzielnik += 1

    return False

def main():
    tab = [0] * N

    for i in range(0, N):
        tab[i] = random.randint(1, N)

    print(tab)
    if skoki(tab):
        print('Da sie')
    else:
        print('Nie da sie')

main()