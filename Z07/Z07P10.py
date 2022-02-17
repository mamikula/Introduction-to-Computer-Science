#Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać
#funkcję dodającą dwie takie liczby. W wyniku dodawania dwóch liczb powinna
#powstać nowa lista.

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
            if nxt:
                nxt = nxt.next

        self.first = prev

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value)
            tmp = tmp.next


ff1 = linked_list()
ff1.insert(9)
ff1.insert(9)
ff1.insert(9)
ff1.insert(9)

ff1.reverse()
#ff1.printlist()

ff2 = linked_list()
ff2.insert(9)
ff2.insert(9)
ff2.insert(9)
ff2.insert(9)
ff2.reverse()
#ff2.printlist()

def addition(f1, f2):
    p = f1
    q = f2
    new = linked_list()
    new_val = 0
    while p != None or q != None:
        #print('1')
        if p and q:
            new_val += p.value + q.value
            p = p.next
            q = q.next
        elif p and not q:
            new_val += p.value
            p = p.next
        elif q and not p:
            new_val += q.value
            q = q.next

        new.insert(new_val % 10)
        new_val //= 10

    if new_val != 0:
        new.insert(new_val)

    new.reverse()
    new.printlist()

    return new

addition(ff1.first, ff2.first)
