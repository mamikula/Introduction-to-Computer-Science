#Kolejne (co najmniej dwa) elementy listy o identycznej wartości pola val nazywamy podlistą stałą. Proszę napisać
#funkcję, która usuwa z listy wejściowej najdłuższą podlistę stałą. Warunkiem jej usunięcia jest istnienie w liście
#dokładnie jednej najdłuższej podlisty stałej. Do funkcji należy przekazać wskaźnik na pierwszy element listy.
#Funkcja powinna zwrócić liczbę usuniętych elementów.
#Na przykład z listy [ 1 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] należy usunąć podlistę [ 2 2 2 2 ],
#a z listy [ 1 3 3 3 3 5 7 11 13 13 1 2 2 2 2 3 ] nie należy nic usuwać.

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

def deleting(first):
    tmp = node()
    tmp.next = first
    first = tmp

    q = first
    p = node()
    z = node()
    p.next = q
    z.next = q
    curlen = 1
    maxlen = 0
    onetodel = True

    while q.next.next:
        if q.next.value != q.next.next.value:
            q = q.next

        elif q.next.value == q.next.next.value:
            z = q

            while q.next.next and q.next.value == q.next.next.value:
                q = q.next
                curlen += 1

            if curlen > maxlen:
                p = z
                maxlen = curlen
                curlen = 1
                onetodel = True

            else:
                if curlen == maxlen:

                    onetodel = False

                curlen = 1

    todel = p.next.value

    if onetodel:
        while p.next and p.next.value == todel:
            tmp = p.next
            p.next = tmp.next
            del tmp

        first = first.next
        printlist(first)
        return maxlen

    else:
        first = first.next
        printlist(first)
        return 0

f1 = node()

#1 3 3 3 5 7 11 13 13 1 2 2 2 2 3



insert(f1, 1)
insert(f1, 2)
insert(f1, 2)
insert(f1, 2)
insert(f1, 1)
insert(f1, 3)
insert(f1, 3)
insert(f1, 3)
insert(f1, 5)
insert(f1, 13)
insert(f1, 13)
insert(f1, 13)
insert(f1, 13)
#insert(f1, 3)
printlist(f1)


#1 3 3 3 3 5 7 11 13 13 1 2 2 2 2 3

f2 = node()
insert(f2, 1)
insert(f2, 3)
insert(f2, 3)
insert(f2, 3)
insert(f2, 3)
insert(f2, 5)
insert(f2, 7)
insert(f2, 11)
insert(f2, 13)
insert(f2, 13)
insert(f2, 1)
insert(f2, 2)
insert(f2, 2)
insert(f2, 2)
insert(f2, 2)
insert(f2, 3)



print(deleting(f1))
