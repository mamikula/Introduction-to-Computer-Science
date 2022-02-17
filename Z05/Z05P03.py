#Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N < 100). Położenie
#hetmanów jest opisywane przez tablicę dane = [(w1, k1),(w2, k2),(w3, k3), ...(wN , kN )] Proszę napisać funkcję,
#która odpowiada na pytanie: czy żadne dwa hetmany się nie szachują? Do funkcji należy przekazać
#położenie hetmanów.

def szachuja_sie(dane):
    #1 nie moze sie szachowac
    if len(dane) < 2:
        return False
    BOK = 100
    plansza = [[False for _ in range(BOK)] for _ in range(BOK)]

    for i in range(0, len(dane)):
        wsp = dane[i]
        plansza[wsp[0]][wsp[1]] = True

    #teraz bedzie sprawdzane czy pionowo, poziomo i ukosnie na drodze jednego hetmana nie stoi drugi

    #poziome i pionowe
    for i in range(0, BOK):
        poziom = False
        pion = False
        for j in range(0, BOK):
            if plansza[i][j]:
                if poziom:
                    return True
                poziom = True

            if plansza[j][i]:
                if pion:
                    return True
                pion = True


    #teraz ukosne
    pocz_w_bok = False
    poczW = 1
    poczK = 0
    while not (poczW == BOK - 1 and poczK == BOK - 1):
        skosl = False
        skosp = False
        w = poczW
        k = poczK
        while w >= 0 and k <= BOK - 1:
            if plansza[w][k]:
                if skosp:
                    return True
                skosp = True

            #odbicie lustrzane wzgledem kolumn
            if plansza[w][BOK - 1 - k]:
                if skosl:
                    return True
                skosl = True

            w -= 1
            k += 1
        #jezeli dotarl do rogu przesuwa sie w prawo zamiast w dol
        if poczW == BOK - 1:
            pocz_w_bok = True

        if pocz_w_bok:
            poczK += 1

        else:
            poczW += 1

    return False


def main():
    #print('Podaj ilosc hetmanow')
    N = int(input())

    dane = [[None for _ in range(N)]for _ in range(N)]
    print('wpisuj wspolrzedne hetmanow')

    #zakladam ze input jest poprawny
    for i in range(0, len(dane)):
        dane[i] = (int(input()), int(input()))
        print(dane[i])

    if szachuja_sie((dane)):
        print('Szachuja sie')
    else:
        print('Nie szaczuja sie')
main()