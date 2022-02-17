#Dana jest liczba naturalna o niepowtarzających się cyfrach pośród których nie ma zera. Ile
#różnych liczb podzielnych np. przez 7 można otrzymać poprzez wykreślenie dowolnych cyfr w tej liczbie. Np.
#dla 2315 będą to 21, 35, 231, 315.

liczba = 2112

def dl_liczby(liczba): # potrzebna do wybierania cyfr z podanej liczby np liczba dlugosc 5 to tak jakby z piecu kratek wybieram cyfry
    licznik = 0
    while liczba > 1:
        liczba //= 10
        licznik += 1

    return licznik

def max_dziesietna(liczba, n): #wszystkie mozliwosci zbioru 4 elementowego
    res = 0
    for i in range(0, n):
        res = res + 2**i

    return res

def dec_to_bin(x): #generuje permutacje zbioru 4 elementowego, binarnego
    res = 1
    while x > 1:
        res = res * 10 + x % 2
        x //= 2

    return res

def reverse(x): #odwraca liczbe
    res = 0
    while x >= 1:
        res = res * 10 + x % 10
        x = x // 10
    return res

def new_liczba_creator(map, liczba, n): #generator liczb wedlug mapy
    res = 0
    for i in range(0, n):
        if map % 10 == 1:
            res = res * 10 + liczba % 10
        liczba = liczba // 10
        map = map // 10
    res = reverse(res)

    return res


def f(liczba):
    n = dl_liczby(liczba)
    maks = max_dziesietna(liczba, n)

    for i in range(0, maks + 1):
        map = dec_to_bin(i)         #generowanie binarnych permutacji o zadanej dlugosci
        tmp = new_liczba_creator(map, liczba, n)
        if tmp % 7 == 0:
            print(tmp)

f(liczba)