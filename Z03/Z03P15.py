#Dana jest duża tablica t. Proszę napisać funkcję, która zwraca informację czy w tablicy
#zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
#liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”
import a as a

N = 10

def prime(a):
    if a == 0 or a == 1:
        return False

    for i in range(2, int(a**0.5) + 1):
        if a % i == 0:
            return False
    return True

def fun(t):
    a = 0
    b = 1
    ess = False

    for i in range(0, N):

        if a < i:
            while a < i:
                b = a + b
                a = b - a

        print(a, b, i)
        if a == i:
            if prime(t[a]):
                 return False
            continue

        elif not ess:
            if prime(t[i]):
                ess = True


    if ess:
        return True

    return False

t = [0, 2, 4, 4, 8, 9, 10, 12, 18, 7]

print(fun(t))