#Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w sensie
#liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów tych elementów.
#Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego podzbioru.
#Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.

def sumy(t, sel, sid, i):
    
    else:
        sumy(t, sel + t[i], sid + i, i + 1)
        sumy(t, sel, sid, i + 1)

t = [1, 7, 3, 5, 11, 2]
sumy(t, 0, 0, 0)