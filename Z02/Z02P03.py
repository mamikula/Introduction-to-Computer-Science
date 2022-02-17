#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
#czy liczba naturalna jest palindromem, a następnie czy jest palindromem w systemie
#dwójkowym.

def bin(liczba):
    bliczba = 1
    while liczba > 1:
        bliczba = (bliczba * 10) + (liczba % 2)
        liczba //= 2
    print(bliczba)
    return bliczba

def palindrom(liczba):
    print(liczba)
    tmp = liczba
    d = 0
    while tmp > 0:
        d = (d * 10) + (tmp % 10)
        tmp //= 10
    if liczba == d:
        print("palindrom w dziesietnym")
    else:
        print("niepalindrom w dziesietnym")

    tmp = liczba = bin(liczba)
    d = 0
    while tmp > 0:
        d = (d * 10) + (tmp % 10)
        tmp //= 10
    if d == liczba:
        print("palindrom w bin")
    else:
        print("Niepalindrom w bin")

liczba = 73
palindrom(liczba)