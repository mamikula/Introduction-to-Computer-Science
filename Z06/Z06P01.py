#Proszę napisać funkcję, która jako argument przyjmuje liczbę całkowitą i wypisuje wszystkie
#co najmniej dwucyfrowe liczby pierwsze, powstałe poprzez wykreślenie z liczby pierwotnej co najmniej jednej
#cyfry.


def pid(a): #pierwsza i dwucyfrowa
    if a <= 10:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True

def generator(dana, nowa, mnoznik):



    if dana == 0:
        if pid(nowa):
            print(nowa)

    else:
            (generator(dana // 10, nowa + (dana % 10) * mnoznik, mnoznik * 10) or
            generator(dana // 10, nowa, mnoznik))

generator(1231, 0, 1)