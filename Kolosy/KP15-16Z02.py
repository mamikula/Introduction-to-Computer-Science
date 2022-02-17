#Dana jest N elementowy zbiór liczb naturalnych w postaci tablicy int t[N]. Proszę napisać
#funkcję, która zwraca informację czy jest możliwy podział zbioru na trzy zbiory tak aby w każdym z
#trzech zbiorów lączna liczba jedynek w liczbach zapisanych w systemie binarnym była jednakowa. Na
#przykład dla zbioru |2,3,5,7,11,13,16} możliwy podział to {2,13,16} {3,11} {5,7} czyli w systemie
#dwójkowym {10,1101,10000} {11,1011} {101',111'} - w każdym zbiorze jest 5 jedynek.


def ones(t):
    for i in range(len(t)):
        cnt = 0
        a = t[i]
        while a > 0:
            if a % 2 == 1:
                cnt +=1
            a //= 2
        t[i] = cnt
    return t

def rekur(t, s1, s2, s3, id):
    if id == len(t):
        return (s1 == s2 == s3)

    return (rekur(t, s1 + t[id], s2, s3, id + 1) or
            rekur(t, s1, s2 + t[id], s3, id + 1) or
            rekur(t, s1, s2, s3 + t[id], id + 1))



def possible():
    t = [2, 3, 5, 7, 11, 13, 16]
    #t = [2, 2, 2]
    t = ones(t)

    tmp = 0
    for i in range(len(t)):
        tmp += t[i]
    if tmp % 3 != 0:
        return False
    return True

print(possible())