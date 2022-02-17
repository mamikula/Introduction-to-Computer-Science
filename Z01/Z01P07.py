#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie, czy
#liczba ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

def ciag():
    liczba = 19
    a = 1
    b = 1
    while b < liczba:
        if liczba % (a * b) == 0 and a * b == liczba:
            print("jest")
            return True
        b = b + a
        a = b - a
    print("Nie jest")
    return False

ciag()