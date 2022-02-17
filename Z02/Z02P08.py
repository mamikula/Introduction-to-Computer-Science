# Pewnych liczb nie można przedstawić jako sumy elementów spójnych fragmentów ciągu
# Fibonacciego, np. 9, 14, 15, 17, 22. Proszę napisać program, który wczytuje liczbę
# naturalną n, wylicza i wypisuje następną taką liczbę większą od n.Można założyć,
# że 0 < n < 1000.

def czy_fib(liczba):
    a = 1
    b = 1
    suma = 0
    while suma < liczba:
        suma = a + b
        b = a + b
        a = b - a
    if suma == liczba:
        return True
    if suma > liczba:
        suma -= a
        b = b + a
        a = b - a
    if suma == liczba:
        return True
    else:
        return False

liczba = 3
while czy_fib(liczba):
    liczba += 1
print(liczba)