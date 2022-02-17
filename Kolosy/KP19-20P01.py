#Dane są deklaracje reprezentujące szachownicę o boku długości N:
#const int N= …
#int tab[N][N];
#Tablica tab jest wypełniona liczbami naturalnymi. Na szachownicy umieszczamy dwa klocki domina tak, że jeden
#klocek przykrywa dwa pola. Proszę napisać funkcję, która sprawdza czy istnie takie ustawianie klocków na
#szachownicy, że:
#- oba klocki są prostopadle do siebie,
#- w żadnym wierszu ani w żadnej kolumnie nie leży więcej niż jeden klocek,
#- największym wspólnym dzielnikiem 4 przykrytych liczb jest jeden.

N = 10
from random import randint

def NWD(a, b):
    while a != b:
        if a > b:
            a = a - b
        elif b > a:
            b = b - a
    return a

def ustawienia(t):
    # koordynatami sa dolna połowa pionowego i lewa czesc poziomego


    for pozX in range(N - 1):
        for pozY in range(N):
            for pionX in range(N - 1):
                for pionY in range(N):

                    #pionowy nie moze byc w pionowej lini z lewa polowa poziomego
                    #pionowy nie mozeby byc w pionowej lini z prawa polowa poziomego
                    #dolna polowa pionowego nie moze byc w poziomej lini z poziomym
                    #gorna polowa pionowego nie moze byc w poziomej lini z poziomym

                    if pionX == pozX or pionX == pozX + 1 or pionY == pozY or pionY + 1 == pozY:
                        continue

                    if NWD(NWD(NWD(t[pionX][pionY], t[pionX + 1][pionY]), t[pozX][pozY]), t[pozX][pozY + 1]) == 1:
                        print(pionX, pionY, pionX + 1, pionY, pozX, pozY, pozX, pozY + 1)
                        return True

    return False

def main():
    t = [[randint(1,10) for _ in range(N)] for __ in range(N)]

    for i in t:
        print(i)

    print(ustawienia(t))

main()