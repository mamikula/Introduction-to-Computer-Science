#Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która
#zwraca wskaźnik do ostatniego elementu przed cyklem.

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

    def before_cycle(self):
        w = self.first
        p = self.first.next
        prev = self.first

        while p.next != w:

            if w == p:
                w = self.first
                p = p.next
            if p.next == w:
                return None

            prev = w
            w = w.next
        print(prev.value)
        return prev

cycl = linked_list()
#cycl.insert(1)
#cycl.insert(2)
#cycl.insert(1)
#cycl.insert(1)
cycl.insert(1)
cycl.insert(0)
cycl.insert(2)
cycl.insert(2)
cycl.insert(2)
cycl.insert(2)
cycl.insert(2)
cycl.insert(2)
cycl.insert_cycle(0)
cycl.before_cycle()