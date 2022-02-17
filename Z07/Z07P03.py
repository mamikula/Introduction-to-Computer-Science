# Proszę napisać funkcję scalającą dwie posortowane listy w jedną
#posortowaną listę. Do funkcji należy przekazać wskazania na pierwsze
#elementy obu list, funkcja powinna zwrócić wskazanie do scalonej listy.
#- funkcja iteracyjna,
#- funkcja rekurencyjna.


class node():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class lods():
    def __init__(self):
        self.first = None


    def insert(self, new_val):
        if self.first == None:
            self.first = node(new_val)
            return

        tmp = self.first
        while tmp.next != None:

            tmp = tmp.next

        if tmp.next == None:
            tmp.next = node(new_val, tmp.next)


    def printlist(self):
        tmp = self.first
        while tmp != None:
            print(tmp.value)
            tmp = tmp.next
        print('\n')



def merge(ff1, ff2):
    new = lods()
    f1 = ff1.first
    f2 = ff2.first
    while f1 != None or f2 != None:
        if f1 != None and (f2 == None or f1.value <= f2.value):
            new.insert(f1.value)
            f1 = f1.next
        else:
            new.insert(f2.value)
            f2 = f2.next
    return new


def merge_rekur(f1, f2):

    if f1 is None: return f2
    if f2 is None: return f1

    if f1.value > f2.value:
        f2.next = merge_rekur(f1, f2.next)
        return f2
    else:
        f1.next = merge_rekur(f1.next, f2)
        return f1

ff1 = lods()
ff1.insert(2)
ff1.insert(4)
ff1.insert(5)
ff1.insert(9)

ff2 = lods()
ff2.insert(1)
ff2.insert(3)
ff2.insert(5)
ff2.insert(6)
ff2.insert(10)

f3 = merge_rekur(ff1.first, ff2.first)
#ff3 = merge(ff1, ff2)
#ff3.printlist()

while f3 is not None:
    print(f3.value, end=" ")
    f3 = f3.next




