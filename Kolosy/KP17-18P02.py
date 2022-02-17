#Dane s¡ dwie tablice int t1[N] oraz int t2[N] wypelnione liczbami naturalnymi. Elementy z tablic t1 i t2
#laczymy w pary (po jednym elemencie z kazdej tablicy) tak, aby suma wybranych elementów z tablicy t1 byla
#równa sumie wybranych elementów z tablicy t2. Prosze napisac funkcje, która zwróci maksymalna liczbe
#par, jaka mozna uzyskac. Do funkcji nalezy przekaza¢ wylacznie tablice t1 i t2, funkcja powinna zwrócic
#maksymalna liczbe par.


def pairs(t1, t2):
    return rekur(t1, t2, 0, 0, 0, 0, 0)

def rekur(t1, t2, id, s1, s2, m1, m2):
    if id == len(t1):
        if s1 == s2 and m1 == m2:
            return m1
        else:
            return 0

    return( max(rekur(t1, t2, id + 1, s1 + t1[id], s2 + t2[id], m1 + 1, m2 + 1),
                rekur(t1, t2, id + 1, s1 + t1[id], s2, m1 + 1, m2),
                rekur(t1, t2, id + 1, s1, s2 + t2[id], m1, m2 + 1),
                rekur(t1, t2, id + 1, s1, s2, m1, m2,)))

t1 = [1, 2, 3, 4, 5]
t2 = [1, 2, 6, 3, 4]

print(pairs(t1, t2))

