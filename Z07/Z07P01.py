
'''Zaimplementuj zbiór mnogościowy liczb naturalnych korzystając ze
struktury listy odsyłaczowej.
- czy element należy do zbioru
- wstawienie elementu do zbioru
- usunięcie elementu ze zbioru'''

class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class list():
    def __init__(self):
        self.first = None

    def insert(self, new_value):

        if self.first == None:
            self.first = node(new_value)
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        if tmp.next == None:
            tmp.next = node(new_value, tmp.next)

    def printlist(self):
        tmp = self.first
        while tmp != None:
            print(tmp.value)
            tmp = tmp.next
        print('\n')

    def does_ins(self, inp):
        tmp = self.first
        while tmp != None:
            if tmp.value == inp:
                return True
            tmp = tmp.next
        return False

    def remove(self, inp):
        p = self.first
        q = p.next

        if self.first.value == inp:
            tmp = self.first
            self.first = self.first.next
            del tmp
        else:
            while q.value != inp:
                p = q
                q = q.next
            p.next = q.next
            del q


start = list()

start.insert(1)
start.insert(3)
start.insert(4)
start.insert(2)
start.printlist()

print(start.does_ins(4))
start.remove(2)
start.printlist()