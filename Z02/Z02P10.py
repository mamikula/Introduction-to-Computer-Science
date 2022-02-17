#. Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
#czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem A(n)=3*A(n-1)+1, a pierwszy wyraz jest równy 2.

def ciag():
    an = 2
    liczba = 23
    if liczba < 2:
        print('Zla liczba')
        return False

    while an <= liczba:
        if liczba % an == 0:
            print("Jest")
            return True
        an = 3 * an + 1

    print("Nie jest")
    return False
ciag()