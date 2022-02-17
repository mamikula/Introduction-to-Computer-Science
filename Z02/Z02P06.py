#Napisać program wczytujący liczbę naturalną z klawiatury i rozkładający ją na
#iloczyn 2 liczb o najmniejszej różnicy. Np. 30=5*6, 120=10*12.

def main():
    liczba = 60
    if liczba <= 0:
        print("Ups")
        return 0
    i = liczba**0.5
    while i >= 1 and liczba % i != 0:
        i += 1
    print(i)
    print(liczba // i)
main()