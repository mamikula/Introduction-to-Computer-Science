#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta zawiera cyfrę równą liczbie swoich cyfr.

def ile(liczba):
    l = 0
    if liczba == 0:
        return l
    while liczba > 0:
        liczba //= 10
        l += 1
    return l

def main():
    liczba = 1233
    l = ile(liczba)
    while liczba > 0:
        if liczba % 10 == l:
            print("zawiera")
            return
        liczba //= 10
    print("nie zawiera")
    return

main()