#Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpowiada
#na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory o
#jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
#wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool

def sumy(t, i, s1, s2, m1, m2, k):

    if i == len(t):
        return m1 + m2 == k and s1 == s2

    else:
        return (sumy(t, i + 1, s1 + t[i], s2, m1 + 1, m2, k) or
                sumy(t, i + 1, s1, s2 + t[i], m1, m2 + 1, k) or
                sumy(t, i + 1, s1, s2, m1, m2, k))

def main():
    #t = [1, 2, 3, 4, 5, 6]
    t = [1, 2, 3, 4, 1, 2]
    print(sumy(t, 0, 0, 0, 0, 0, 7))

main()