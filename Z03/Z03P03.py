#Napisać program generujący i wypisujący liczby pierwsze mniejsze
#od N metodą Sita Eratostenesa

def sito():
    n = 100
    tab = [True]*(n+1)

    for i in range(2, n + 1, 1):
        if tab[i] == True:
            for j in range(i + i, n + 1, i):
                tab[j] = False

    for i in range(2, n + 1):
       if tab[i]:
           print(i)

sito()