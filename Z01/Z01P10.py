#Napisać program wyszukujący liczby doskonałe mniejsze od miliona.

#Liczba doskonała - to taka liczba naturalna,
#która jest równa sumie wszystkich swoich podzielników, mniejszych od tej liczby.

def dosk():

    for i in range(2, 1000000):
        suma = 0
        for j in range(1, i):
            if i % j == 0:
                suma += j
        if suma == i:
            print(i)
