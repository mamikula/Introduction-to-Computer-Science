#Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca
#kolejność jej elementów.


class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class chain:
    def __init__ (self):
        self.first = None

    def insert(self, new_val):
        if self.first is None:
            self.first = node(new_val)
            return

        tmp = self.first
        while tmp.next is not None:
            tmp = tmp.next

        if tmp.next == None:
            tmp.next = node(new_val)

    def reverse(self):
        if self.first is None or self.first.next is None:
            return

        prev = None
        curr = self.first
        nxt = self.first.next

        while curr:
            curr.next = prev
            prev = curr
            curr = nxt
            if nxt != None:
                nxt = nxt.next

        self.first = prev

    def printlist(self):
        tmp = self.first
        while tmp != None:
            print(tmp.value, end = " ")
            tmp = tmp.next
        print('\n')

arr = chain()
arr.insert(1)
arr.insert(1)
arr.insert(1)
arr.insert(3)
arr.insert(5)
arr.printlist()
arr.reverse()
arr.printlist()

