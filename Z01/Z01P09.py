#Napisać program wypisujący podzielniki liczby.


def podzielniki():
    dana = 120
    for i in range(1, dana + 1):
        if dana % i == 0:
            print(i)

podzielniki()