#Dana jest tablica t[N] zawieraj¡ca liczby naturalne. Prosz¦ napisa¢ funkcj¦, która odpowiada na pytanie,
#czy z elementów tablicy (niekoniecznie wszystkich) mo»na utworzy¢ dwa równoliczne, niepuste podzbiory
#o jednakowej sumie elementów. Do funkcji nale»y przekaza¢ wylacznie tablice t, funkcja powinna zwróci¢
#warto±¢ typu bool.

def sums(t, s1, m1, s2, m2, id):

    if id == len(t):
        print(s1, s2)
        return s1 == s2 and m1 == m2 and s1 != 0

    return( sums(t, s1 + t[id], m1 + 1, s2, m2, id + 1) or
            sums(t, s1, m1, s2 + t[id], m2 + 1, id + 1) or
            sums(t, s1, m1, s2, m2, id + 1))



t = [1, 2, 2, 5]

print(sums(t, 0, 0, 0, 0, 0))