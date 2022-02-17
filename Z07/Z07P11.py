#11. Lista zawiera niepowtarzające się elementy. Proszę napisać funkcję do
#której przekazujemy wskaźnik na początek oraz wartość klucza. Jeżeli
#element o takim kluczu występuje w liście należy go usunąć z listy. Jeżeli
#elementu o zadanym kluczu brak w liście należy element o takim kluczu
#wstawić do listy.

class node:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

class linked_list:
    def __init__(self):
        self.first = None

    def insert(self, new_key):
        if self.first == None:
            self.first = node(new_key)
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        if tmp.next == None:
            tmp.next = node(new_key)

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.key)
            tmp = tmp.next

    def exists(self, iskey):
        if self.first.key == iskey:
            if self.first.next == None:
                self.first = None
                return
            else:
                tmp = self.first
                self.first = self.first.next
                del tmp
                return
        p = self.first
        while p.next:
            if p.next.key == iskey:
                tmp = p.next
                p.next = tmp.next
                del tmp
                return
            p = p.next
        self.insert(iskey)

f1 = linked_list()
f1.insert(5)
#f1.insert(2)
#f1.insert(3)
f1.insert(4)
f1.exists(5)
f1.printlist()

