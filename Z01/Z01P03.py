#Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej
#sumie

def fib():
    a1 = 0
    b1 = 1
    a2 = 0
    b2 = 1
    suma = 0
    szukana = int(input())
    while b1 <= szukana:
        if suma == szukana:
            print("Istnieje")
            return 0
        if suma < szukana:
            suma += b1
            b1 = b1 + a1
            a1 = b1 - a1
        elif suma > szukana:
            suma -= b2
            b2 = b2 + a2
            a2 = b2 - a2
    print("Nie istnieje")
    return 0
fib()