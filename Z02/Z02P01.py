#Napisz program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
#czy liczba ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.

def main():
    liczba = int(input("Podaj liczbe: "))
    a = 1
    b = 1
    while a <= liczba:
        if liczba % a == 0:
            liczba2 = liczba / a
            a2 = b
            b2 = a + b
            while a2 <= liczba2:
                if a2 == liczba2:
                    print("Jest")
                    return True
                else:
                    b2 = a2 + b2
                    a2 = b2 - a2
        b = a + b
        a = b - a
    print("Nie jest")
    return False

main()
