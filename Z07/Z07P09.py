#Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne
#elementy listy przechowują kolejne cyfry. Proszę napisać funkcję
#zwiększającą taką liczbę o 1.

class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

class linked_list:
    def __init__(self):
        self.first = None

    def insert(self, new_val):
        if self.first == None:
            self.first = node(new_val)
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        if tmp.next == None:
            tmp.next = node(new_val)

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value)
            tmp = tmp.next


    def addition(self):
        p = self.first
        q = self.first

        while p.next:
            if p.value != 9:
                q = p
            p = p.next

        if p.value == 9:
            if q.value == 9:
                q.value = 1
                q = q.next
                while q:
                    q.value = 0
                    q = q.next
                self.insert(0)

            else:
                q.value += 1
                q = q.next
                while q:
                    q.value = 0
                    q = q.next

        else:
            p.value += 1




f3 = linked_list()
f3.insert(8)
f3.insert(9)
f3.insert(9)
f3.insert(9)
f3.addition()
f3.printlist()