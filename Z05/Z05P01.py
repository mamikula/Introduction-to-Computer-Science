#Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca
#licznik, m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
#m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie.

#nalezy zmodyfikowac, zalezy co ma zwracac i co wyswietlac, napisane raczej pogladowo zeby sprawdzic czy dziala

def NWD(a, b):
    a = abs(a)
    b = abs(b)
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a

def NWW(a, b):
    return a*b//NWD(a, b)

def ulamek_podaj():
    licznik = int(input())
    mian = int(input())
    while mian == 0:
        print("nie mozna dzielic przez 0!!")
        print("podaj mianownik jeszcze raz")
        mian = int(input())

    return(licznik, mian)

def wypisz(u):
    print(u[0],'/', u[1], end='')
    print('\n')

def skracanie(u):
    skr = NWD(u[0], u[1])
    l = u[0] // skr
    m = u[1] // skr
    return(l, m)

def dodawanie(u1, u2):
    n = NWW(u1[1], u2[1])
    l = u1[0]*n//u1[1] + u2[0]*n//u2[1]
    if l == 0:
        print(0, '\n')
        return 0
    m = u1[0]*n
    u3 = (l, m)
    skracanie(u3)
    wypisz(u3)
    return(l, m)

def odejmowanie(u1, u2):
    l = -u2[0]
    m = u2[1]
    u3 = (l, m)
    dodawanie(u1, u3)

def mnozenie(u, v):
    l = u[0] * v[0]
    m = u[1] * v[1]
    c = (l, m)
    skracanie(c)
    wypisz(c)
    return(l, m)

def dzielenie(u, v):
    l = v[1]
    m = v[0]
    c = (l, m)
    mnozenie(v, c)

def potegowanie(u, w):
    l = 1
    m = 1
    while w > 0:
        l *= u[0]
        m *= u[1]
        w -= 1
    c = (l, m)
    skracanie(c)
    wypisz(c)
    return c

u1 = ulamek_podaj()
u2 = ulamek_podaj()
u1 = skracanie(u1)
u2 = skracanie(u2)
dodawanie(u1, u2)
odejmowanie(u1, u2)
mnozenie(u1, u2)
dzielenie(u1, u2)
potegowanie(u1, 4)
#wypisz(u)