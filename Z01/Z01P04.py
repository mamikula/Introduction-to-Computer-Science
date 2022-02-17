#Proszę napisać program obliczający pierwiastek całkowitoliczbowy z liczby naturalnej
#korzystając z zależności 1 + 3 + 5 + ... = n^2


def pierN():
    liczba = int(input())
    sqrt = 0
    wynik = -1
    i = 1
    while sqrt <= liczba:
        sqrt = sqrt + i
        i += 2
        wynik += 1
    print(wynik)
pierN()
