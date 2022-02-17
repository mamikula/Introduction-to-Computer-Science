#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający
#na pytanie,
#czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem
#A(n)=n*n+n+1.

def main():
    liczba = int(input("Podaj liczbe: "))
    n = 1
    an = n * n + n + 1
    while an <= liczba:
        if liczba % an == 0:
            print("Jest")
            return True
        n += 1
        an = n * n + n + 1
    print("Nie jest")
    return False

main()