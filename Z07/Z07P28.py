#Dwie listy zawierają niepowtarzające się (w obrębie listy) liczby
#naturalne. W pierwszej liście liczby są posortowane rosnąco, a w drugiej
#nie. Proszę napisać funkcję usuwającą z obu list liczby występujące w obu
#listach. Do funkcji należy przekazać wskazania na obie listy, funkcja
#powinna zwrócić łączną liczbę usuniętych elementów.

class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class linked_list:
    def __init__(self):
        self.first = None


    def insert(self, num):
        if self.first == None:
            self.first = node(num)
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        tmp.next = node(num)


    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end = " ")
            tmp = tmp.next
        print('\n')

def two_lists(f1, f2):

    war = node()
    war.next = f1.first
    f1.first = war

    car = node()
    car.next = f2.first
    f2.first = car

    cnt = 0
    p = f1.first # posortowana

    while p.next:
        q = f2.first
        todel = False

        while q.next:

            if q.next.value == p.next.value:
                tmp = q.next
                q.next = tmp.next
                del tmp
                todel = True
                break

            q = q.next

        if todel:
            cnt += 2
            tmp = p.next
            p.next = tmp.next
            del tmp

        else:
            p = p.next

    f1.first = f1.first.next
    f2.first = f2.first.next
    return cnt



f1 = linked_list()
f2 = linked_list()

f1.insert(0)
f1.insert(1)
f1.insert(2)
f1.insert(3)
f1.insert(9)

f2.insert(0)
f2.insert(3)
f2.insert(1)
f2.insert(5)
f2.insert(8)
f2.insert(6)
f2.insert(2)

print("Usunieto: ",two_lists(f1, f2))
f1.printlist()
f2.printlist()