# Dane są dwa niepuste łańcuchy odsyłaczowe [jednokierunkowe] przechowujące liczby
#naturalne. W pierwszym liczby są uporządkowane rosnąco, a w drugim malejąco. Proszę
#napisać odpowiednie definicje typów oraz funkcję scalającą takie dwa łańcuchy w jeden
#zawierający posortowane rosnąco elementy. Funkcja powinna zwrócić wskaźnik do nowego
#łańcucha.

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


def putinside(f1, num):
    while f1.next.value < num:
        f1 = f1.next

    tmp = node(num)
    tmp.next = f1.next
    f1.next = tmp


def printlist(first):
    while first:
        print(first.value, end =" ")
        first = first.next
    print()


def merge(f1, f2):
    tmp1 = node()
    tmp1.next = f1
    f1 = tmp1
    tmp2 = node()
    tmp2.next = f2
    f2 = tmp2

    q = f2

    while q.next:
        p = f1
        tmp = node(q.next.value)
        while p.next != None and p.next.value < q.next.value:
            p = p.next

        if p.next == None:
            p.next = node(q.next.value)

        else:
            tmp.next = p.next
            p.next = tmp

        q = q.next

    f1 = f1.next
    printlist(f1)
    #printlist(f2)
    return f1


f1 = node()
insert(f1, 1)
insert(f1, 3)
insert(f1, 5)
insert(f1, 7)
insert(f1, 9)

printlist(f1)
#delfirst(f1)


f2 = node()
insert(f2, 10)
insert(f2, 8)
insert(f2, 6)
insert(f2, 4)
insert(f2, 2)
insert(f2, 0)
printlist(f2)

merge(f1, f2)