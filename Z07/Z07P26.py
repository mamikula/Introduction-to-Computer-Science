#Proszę napisać funkcję, która sprawdza czy jedna lista zawiera się w
#drugiej. Do funkcji należy przekazać wskazania na pierwsze elementy obu
#list, funkcja powinna zwrócić wartość logiczną.

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


    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end = " ")
            tmp = tmp.next
        print('\n')

def contain(f1, f2):

    p = f1
    q = f2

    while p and q:
        if q.value == p.value:
            p = p.next
        q = q.next
        if p == None:
            return True

    p = f2
    q = f1

    while p and q:
        if q.value == p.value:
            p = p.next
        q = q.next
        if p == None:
            return True

    return False

f1 = linked_list()
f2 = linked_list()

f1.insert(0)
f1.insert(2)
f1.insert(3)
f1.insert(0)

f2.insert(0)
f2.insert(1)
f2.insert(0)
f2.insert(2)
f2.insert(0)
f2.insert(3)
f2.insert(0)
f2.insert(1)

print(contain(f1.first, f2.first))