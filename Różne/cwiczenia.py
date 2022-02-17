class node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

    print()

def repair(p):
    cnt = 0
    #szukanie różnicy
    tmp = p
    r = (p.val - p.next.val)
    while tmp.next:
        if abs(tmp.val - tmp.next.val) < r:
            r = abs(tmp.val - tmp.next.val)
        tmp = tmp.next

    #sprawdzanie znaku
    if p.val - p.next.val < 0:
        r = -r

    tmp = p
    while tmp.next.val != None:
        print(tmp.val)
        if abs(tmp.val - tmp.next.val) > abs(r):
            cnt += 1
            new = node(tmp.val + r)
            new.next = tmp.next
            tmp.next = new
        else:
            tmp = tmp.next

    return cnt

f1 = node()
insert(f1, 1)
insert(f1, 3)
insert(f1, 5)
insert(f1, 7)
insert(f1, 8)

print(repair(f1))


'''
#Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułamki reprezentowane
#są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję longest(T), zwracającą
#długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny. W przypadku gdy
#w tablicy nie ma ciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0.
#Komentarz: Można założyć, że tablica wejściowa liczy więcej niż 2 elementy.
#Przykłady:
#print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] ) # wypisze 4
#print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] ) # wypisze 3
#print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] ) # wypisze 6
#print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] ) # wypisze 0


def longest(T):
    counter = 2
    maxlen = 2
    for i in range(len(T) - 2):
        a1 = T[i]
        a2 = T[i + 1]
        a3 = T[i + 2]
        new1 = (a1[0] * a2[1], a1[1] * a2[0])
        new2 = (a2[0] * a3[1], a2[1] * a3[0])

        if new1[1] != 0 and new2[1] != 0 and (new1[0] / new1[1]) == (new2[0] / new2[1]):
            counter += 1

        else:
            if maxlen < counter:
                maxlen = counter
                counter = 2

    if maxlen < counter:
        maxlen = counter

    if maxlen <= 2:
        return 0
    return maxlen


T1 = [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)]
T2 = [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)]
T3 = [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)]
T4 = [(1,2),(2,3),(3,4),(4,5),(5,6)]

print(longest(T1))
print(longest(T2))
print(longest(T3))
print(longest(T4))

'''

#Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na kawałki, tak aby każdy
#kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję cutting(s), która zwraca liczbę
#sposobów pocięcia słowa na kawałki.
#Przykłady:
#print(cutting(’student’)) # wypisze 2 bo stu-dent, stud-ent
#print(cutting(’sesja’)) # wypisze 3 bo se-sja, ses-ja, sesj-a
#print(cutting(’ocena’)) # wypisze 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a,
#print(cutting(’informatyka’)) # wypisze 36

'''





















