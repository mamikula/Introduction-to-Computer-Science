#Dana jest lista, który być może zakończona jest cyklem.
#Napisać funkcję, która sprawdza ten fakt.

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


    def insert_cycle(self, num):

        tmp = self.first
        while tmp.value != num:
            tmp = tmp.next

        tmp2 = tmp
        while tmp2.next:
            tmp2 = tmp2.next

        tmp2.next = tmp

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end = " ")
            tmp = tmp.next
        print('\n')


    def has_cycle(self):
        p = self.first
        q = self.first.next
        while p.next and q.next.next:
            p = p.next
            q = q.next.next
            if p == q:
                return True
        return False

cycl = linked_list()
cycl.insert(1)
cycl.insert(2)
cycl.insert(3)
cycl.insert(4)
cycl.insert(4)
cycl.insert(4)

cycl.insert_cycle(3)
print(cycl.has_cycle())
#cycl.printlist()