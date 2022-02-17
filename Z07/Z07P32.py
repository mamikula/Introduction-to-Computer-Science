#Lista reprezentuje wielomian o współczynnikach całkowitych. Elementy w
#liście ułożone są według rosnących potęg. Proszę napisać funkcję
#obliczającą różnicę dwóch dowolnych wielomianów. Wielomiany reprezentowane
#są przez wyżej opisane listy. Procedura powinna zwracać wskaźnik do nowo
#utworzonej listy reprezentującej wielomian wynikowy. Listy wejściowe
#powinny pozostać niezmienione.

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

def polynomials(w1, w2):
    w3 = linked_list()
    p = node()
    q = node()
    p.next = w1
    q.next = w2
    while p.next and q.next:
        w3.insert(p.next.value - q.next.value)
        p = p.next
        q = q.next

    while p.next != None:
        p = p.next
        w3.insert(p.value)

    while q.next != None:
        q = q.next
        w3.insert(-q.value)

    w3.printlist()
    return w3

w1 = linked_list()
w2 = linked_list()

w1.insert(1)
w1.insert(2)
w1.insert(3)
#w1.insert(3)
#w1.insert(7)
#w1.insert()

w2.insert(2)
w2.insert(3)
w2.insert(1)
w2.insert(4)

polynomials(w1.first, w2.first)