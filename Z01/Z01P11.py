#Napisać program wyszukujący liczby zaprzyjaźnione mniejsze od miliona.

def sd(liczba):
    suma = 0
    for i in range(1, liczba):
        if liczba % i == 0:
            suma += i
    return suma

def zaprzyjaznione():
    for i in range(2, 10000):
        si = sd(i)
        if si != i:
            s2 = sd(si)
            if s2 != si and s2 == i:
                print(i, si)
    si = 0

zaprzyjaznione()