#Dane są ciągi an, bn i cn określone następująco:
#an = 1 dla n = 1, 2 bn = 1 dla n = 1, 2, 3
#an = an−1 + an−2 dla n > 2 bn = bn−1 + bn−2 + bn−3 dla n > 3
#Wyrazy ciągu cn są kolejnymi liczbami naturalnymi należącymi do ciągu an lub bn.
#Ciągi te przyjmują wartości:
#an : 1 1 2 3 5 8 13 21 ...
#bn : 1 1 1 3 5 9 17 31 ...
#cn : 1 2 3 5 8 9 13 17 ...
#Proszę napisać program który wczytuje wprowadzoną z klawiatury liczbę naturalną k
#i wypisuje k-ty wyraz ciągu cn.

def ciagi(k):
    a = 1
    b = 1
    c = 1
    e = 1
    f = 1
    tmp = True
    while k + 2 > 0:
        cn = min(a, e)

        if a <= cn:
            c = a + b + c
            b = c - b - a
            a = c - b - a

        if e <= cn:
            e = e + f
            f = e - f

        if a != 1 and e >= 1:
            print(cn)

        k -= 1

ciagi(15)