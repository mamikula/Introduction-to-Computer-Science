#Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
#naturalne. W obu listach liczby są posortowane rosnąco. Proszę napisać
#funkcję usuwającą z każdej listy liczby nie występujące w drugiej. Do
#funkcji należy przekazać wskazania na obie listy, funkcja powinna zwrócić
#łączną liczbę usuniętych elementów.

class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class linked_list:
    def __init__(self):
        self.first = None


    def insert(self, num):
        if self.first is None:
            self.first = node(num)
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        tmp.next = node(num)


    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end =" ")
            tmp = tmp.next
        print('\n')

def uniq(f3, f4):

    war = node()
    war.next = f3
    f3 = war
    car = node()
    car.next = f4
    f4 = car

    p = f3
    q = f4
    cnt = 0

    while p.next and q.next:
        if p.next.value < q.next.value:
            tmp = p.next
            p.next = tmp.next
            del tmp
            cnt += 1

        elif p.next.value > q.next.value:
            tmp = q.next
            q.next = tmp.next
            del tmp
            cnt += 1

        else:
            p = p.next
            q = q.next

    if p.next != None:
        while p.next:
            tmp = p.next
            p.next = tmp.next
            del tmp
            cnt += 1

    if q.next != None:
        while q.next:
            tmp = q.next
            q.next = tmp.next
            del tmp
            cnt += 1
    print(f3.next.value, f4.next.value)
    f1.first = f3.next
    f2.first = f4.next

    return cnt

f1 = linked_list()
f2 = linked_list()

f1.insert(1)
f1.insert(3)
f1.insert(6)
f1.insert(8)
f1.insert(10)
f1.insert(12)
f1.insert(14)

f2.insert(2)
f2.insert(4)
f2.insert(6)
f2.insert(7)
f2.insert(9)
f2.insert(11)
f2.insert(13)

f1.printlist()
f2.printlist()

print(uniq(f1.first, f2.first), '\n')

f1.printlist()
f2.printlist()