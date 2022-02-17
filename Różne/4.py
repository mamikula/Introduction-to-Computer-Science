class Node:
    def __init__(self, _value=None, _next=None):
        self.value = _value
        self.next = _next
###


class List:
    def __init__(self):
        self.first = None

    def insert(self, new_value):

        if self.first == None:
            self.first = Node(new_value)
            return

        ptr = self.first
        while ptr.next != None and ptr.next.value < new_value:
            ptr = ptr.next

        if ptr.next == None or ptr.next.value != new_value:
            ptr.next = Node(new_value, ptr.next)

    def reverse(self):

        if self.first == None or self.first.next == None:
            return

        a = None
        b = self.first
        c = b.next

        while b != None:
            b.next = a
            a = b
            b = c
            if c != None:
                c = c.next

        self.first = a

    def reverse_r(self, node=None, previous=None):
        if node == None:
            node = self.first

        next = node.next
        node.next = previous

        if next == None:
            self.first = node
            return

        self.reverse_r(next, node)

    def print(self):

        ptr = self.first
        while ptr != None:
            print(ptr.value)
            ptr = ptr.next

###


t = List()
t.insert(2)
t.insert(5)
t.insert(10)
t.insert(3)
t.insert(4)
t.insert(5)
t.insert(5)
t.insert(7)
t.insert(3)

t.reverse_r()
t.reverse()

t.print()
