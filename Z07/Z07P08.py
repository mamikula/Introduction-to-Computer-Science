#Dana jest niepusta lista, proszę napisać funkcję usuwającą co drugi
#element listy. Do funkcji należy przekazać wskazanie na pierwszy element
#listy.


class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self):
        self.first = None

    def insert(self, val):
        if self.first == None:
            self.first = node(val)
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        if tmp.next == None:
            tmp.next = node(val)

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value)
            tmp = tmp.next

    def cutting(self):
        if self.first == None or self.first.next == None:
            return

        prev = self.first
        while prev:
            #print(prev.value)
            curr = prev.next
            if prev.next != None:
                prev.next = curr.next
            else:
                prev.next = None
            del curr
            prev = prev.next


f1 = linked_list()
f1.insert(1)
f1.insert(2)
f1.insert(3)
f1.insert(4)
f1.insert(5)
#f1.insert(6)
#f1.insert(7)
#f1.insert(8)
#f1.insert(9)
#f1.insert(10)
f1.cutting()
f1.printlist()