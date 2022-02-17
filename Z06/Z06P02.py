#”Waga” liczby jest określona jako ilość różnych czynników pierwszych liczby. Na przykład
#waga(1)=0, waga(2)=1, waga(6)=2, waga(30)=3, waga(64)=1. Dana jest tablica T[N] zawierająca liczby
#naturalne. Proszę napisać funkcję, która sprawdza czy można elementy tablicy podzielić na 3 podzbiory o
#równych wagach. Do funkcji należy przekazać wyłącznie tablicę, funkcja powinna zwrócić wartość typu Bool.

def waga(a):
    ctr = 0
    for i in range(2, a + 1):
        if a % i == 0:
            while a % i == 0:
                a //= i
        ctr += 1
    return ctr

def podzbiory(t, p1, p2, p3, i):
    if i == len(t):
        return (p1 == p2) and (p2 == p3)

    return (podzbiory(t, p1 + t[i], p2, p3, i + 1) or
            podzbiory(t, p1, p2 + t[i], p3, i + 1) or
            podzbiory(t, p1, p2, p3 + t[i], i + 1))




def funkcja(tab):
    t = [i for i in tab]
    suma = 0
    for i in range(len(t)):
        t[i] = waga(tab[i])
        suma += t[i]

    #jezeli suma wag nie jest podzielna przez 3 to nie da sie uzyskac 3 zbiorow o takiej samej sumie
    if suma % 3 != 0:
        return False

    return podzbiory(t, 0, 0, 0, 0)




tab = [-1, 2, 3, 4]
print(funkcja(tab))




