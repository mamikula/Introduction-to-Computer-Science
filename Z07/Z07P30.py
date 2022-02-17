#Dane są dwie niepuste listy, z których każda zawiera niepowtarzające
#się elementy. Elementy w pierwszej liście są uporządkowane rosnąco, w
#drugiej elementy występują w przypadkowej kolejności. Proszę napisać
#funkcję, która z dwóch takich list stworzy jedną, w której uporządkowane
#elementy będą stanowić sumę mnogościową elementów z list wejściowych.
#Do funkcji należy przekazać wskazania na obie listy, funkcja powinna
#zwrócić wskazanie na listę wynikową. Na przykład dla list:
#2 -> 3 -> 5 ->7-> 11
#8 -> 2 -> 7 -> 4
#powinna pozostać lista:
#2 -> 3 -> 4 -> 5 ->7-> 8 -> 11

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


def paste(one, two):

    var = node()
    var.next = one
    one = var

    var2 = node()
    var2.next = two
    two = var2

    q = two

    while q.next:
        p = one
        tmp = node(q.next.value)

        while p.next != None and p.next.value < q.next.value:
            p = p.next

        if p.next == None:

            tmp.next = None
            p.next = tmp

        elif p.next.value == q.next.value:
            q = q.next
            continue

        else:
            tmp.next = p.next
            p.next = tmp

        q = q.next

    f1.first = one.next
    f2.first = two.next

    return


f1 = linked_list()
f2 = linked_list()

f1.insert(1)
f1.insert(2)
f1.insert(3)
f1.insert(5)
f1.insert(7)
f1.insert(9)
f1.insert(11)
f1.insert(13)

f2.insert(2)
f2.insert(3)
f2.insert(4)
f2.insert(6)
f2.insert(8)
f2.insert(10)
f2.insert(12)
f2.insert(14)

#f1.printlist()
#f2.printlist()
paste(f1.first, f2.first)
f1.printlist()
#f2.printlist()




