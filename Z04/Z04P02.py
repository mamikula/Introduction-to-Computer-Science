#Dana jest tablica int t[MAX][MAX] wypełniona liczbami naturalnymi. Proszę napisać
#funkcję który odpowiada na pytanie, czy w każdym wierszu tablicy występuje co
#najmniej jedna liczba złożona wyłącznie z nieparzystych cyfr.
import random



def istnieje():
    N = 2
    t = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            t[i][j] = random.randint(2,2)
            print(t[i][j], end=' ')
        print("\n")

    for w in range(N):
        niep = False
        for k in range(N):
            para = False #jezeli chociaz jedna parzysta to koniec
            liczba = t[w][k]
            while liczba > 0:  #or liczba == 0: naturalne, wiec raczej nie trzeba tego dodawac
                if liczba % 2 == 0:
                    para = True
                    break
                else:
                    liczba //= 10

            if not para: #jezeli dla ktorejs liczby para == false to znaczy ze ma wszystkie cyfry nieparzyste
                niep = True
                break

        if not niep: #jezeli w danym wierszu nie ma liczby o wszystkich cyfrach nieparzystych to nie trzeba sprawdzac dalej
            print("Nie")
            return 0

    print('Tak')
    return 0

istnieje()