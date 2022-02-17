#Mamy cykliczną listę zawierającą liczby całkowite. Każda pierwsza cyfra kolejnej liczby jest równa
#ostatniej cyfrze poprzedniej liczby.
#np. 123 - 324 - 435 - 578 -> łańcuch się zapętla
#Napisz funkcję wstawiającą liczbę do listy. Liczba ma zastąpić dwie już istniejące elementy cyklu.
#dla przykładu tutaj, za (324 - 435) można wstawić 35
#Funkcja powinna zwrócić wartość logiczną w zależności od tego czy próba wstawiania zakończyła się
#sukcesem.

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
    while first:
        print(first.value, end =" ")
        first = first.next
    print()

def printcycle(first):
    tmp = first
    while True:
        print(tmp.value, end =" ")
        tmp = tmp.next
        if tmp == first:
            return

def makecycle(first):
    tmp = first
    while tmp.next:
        tmp = tmp.next

    tmp.next = first


def fn(a):
    while a > 10:
        a //= 10
    return a


def fun(f1, num):

    p = f1
    p = p.next
    start = False
    while True:
        if start:
            break

        if p == f1:
            start = True
        #print(p.value)
                #324 35 435
        #print(fn(p.next.value), fn(num), num % 10, fn(p.next.next.value))
        if fn(p.next.value) == fn(num) and num % 10 == p.next.next.value % 10:
            p.next.value = num
            p = p.next
            tmp = p.next
            p.next = tmp.next
            del tmp

            return True

        p = p.next

    return False




f1 = node()
insert(f1, 123)
insert(f1, 324)
insert(f1, 435)
insert(f1, 578)
#insert(f1, )
makecycle(f1)
#printlist(f1)
printcycle(f1)

print(fun(f1, 53))
