#W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy króla
#nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra liczby na
#polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do obranego celu
#(np. narożnika) król nie może wykonać ruchu, który powoduje oddalenie go od celu. Dana jest globalna tablica
#T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik ma współrzędne
#w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do prawego dolnego
#narożnika.

from random import randint
T = []
ys = []

def cyferki(pierwsza, ostatnia):
    while pierwsza > 10:
        pierwsza //= 10
    if pierwsza > (ostatnia % 10):
        return True

    return False

def droga_krola(w, k):
    print(w, k, T[w][k])
    if (w, k) == (7, 7):
        return True

    wynik = False
    for ruch in [(0, 1), (1, 1), (1, 0), (1, -1), (-1, 1)]:

        i = ruch[0]
        j = ruch[1]

        if w + i < 8 and w + i >= 0 and k + j >= 0 and k + j < 8 and cyferki(T[w + i][k + j], T[w][k]) and ys[w + i][k + j] == 0:

            ys[w + i][k + j] = 1
            if droga_krola(w + i, k + j):

                wynik = True
    return wynik


for i in range(8):
    tmp = []
    tmp2 = []
    for j in range(8):
        tmp.append(randint(1, 100))
        tmp2.append(0)
    print(tmp)
    T.append(tmp)
    ys.append(tmp2)
print(droga_krola(0, 0))
