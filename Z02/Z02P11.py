#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
#czy jej cyfry stanowią ciąg rosnący.

def ciag():
    liczba = 123456
    while liczba > 0:
        a = liczba % 10
        liczba //= 10
        if a <= liczba % 10:
            print('Nie stanowia')
            return

    print('Stanowia')

ciag()