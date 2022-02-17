#Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
#początek listy dwukierunkowej, usuwa z niej wszystkie elementy, w których
#wartość klucza w zapisie binarnym ma nieparzystą ilość jedynek.

class node:
    def __init__(self, value = None, next = None, prev = None):
        self.value = value
        self.next = next
        self.prev = prev

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

        tmp.next = node(new_val)

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end = " ")
            tmp = tmp.next
        print('\n')

    def remove(self):
        if self.first == None:
            return

        p = node()
        p.next = self.first
        while p.next:

            if ones(p.next.value):
                q = p.next

                if p.next == self.first:
                    self.first = q.next

                p.next = q.next
                if q.next != None:
                    q.next.prev = p
                del q
            else:
                p = p.next

def ones(num):
    counter = 0
    while num > 0:
        counter += num % 2
        num //= 2
    if counter % 2 == 1:
        return True
    return False

lid = linked_list()
lid.insert(0)
lid.insert(2)
lid.insert(3)
lid.insert(4)
lid.insert(5)
lid.insert(6)
lid.insert(1)
lid.printlist()
lid.remove()
lid.printlist()