#Zbiór liczb naturalnych jest reprezentowany jako jednokierunkowa lista. Y-lista to struktura
#reprezentująca dwa zbiory liczb naturalnych (rysunek).

#Proszę napisać funkcję, która dwa zbiory A,B reprezentowane jako Y-lista przekształca w dwa
#zbiory reprezentowane jako niezależne listy. Do funkcji należy przekazać wskaźniki do dwóch
#list, funkcja powinna zwrócić liczbę elementów części wspólnej zbiorów A,B.
#Uwagi:
#- ważne: jeżeli część wspólna dwóch zbiorów jest pusta, Y-lista staje się dwoma niezależnymi
#listami.
#- wartości w listach nie są uporządkowane

class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

def insert(first, num):
    if first.value == None:
        first.value = num
        return
    tmp = first
    while tmp.next:
        tmp = tmp.next

    tmp.next = node(num)

def printlist(first):
    tmp = first
    while tmp:
        print(tmp.value, end = " ")
        tmp = tmp.next
    print()

def ylista(f1, f2, num):
    while f1.next:
        f1 = f1.next

    while f2.next:
        f2 = f2.next

    tmp = node(num)
    f1.next = tmp
    f2.next = tmp

def separating(f1, f2):

    newf1 = node()
    newf2 = node()
    cnt = 0
    p = f1

    while p.next:
        q = f2
        while q.next and q != p:
            q = q.next

        if q == p:
            break

        p = p.next

    count = False
    while f1:
        insert(newf1, f1.value)

        if f1 == p and p.next != None:
            count = True
            cnt += 1

        elif count:
            cnt += 1

        f1 = f1.next

    while f2:
        insert(newf2, f2.value)
        f2 = f2.next

    printlist(newf1)
    printlist(newf2)
    return cnt

f1 = node()
insert(f1, 5)
insert(f1, 11)

f2 = node()
insert(f2, 13)
insert(f2, 7)
insert(f2, 17)
ylista(f1, f2, 3)

insert(f1, 2)
insert(f1, 5)
insert(f1, 6)
#printlist(f1)
#printlist(f2)

print(separating(f1, f2))