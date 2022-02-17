#Elementy w liście są uporządkowane według wartości klucza. Proszę
#napisać funkcję usuwającą z listy elementy o nieunikalnym kluczu. Do
#funkcji przekazujemy wskazanie na pierwszy element listy,
#funkcja powinna zwrócić liczbę usuniętych elementów.

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
            print(tmp.value, end=" ")
            tmp = tmp.next
        print('\n')

    def uniq(self):
        counter = 0
        war = node()
        war.next = self.first
        self.first = war

        p = self.first.next
        r = self.first
        while p.next != None:
            if p.value == p.next.value:
                x = p.value
                q = p.next

                while q != None and q.value == x:
                    p.next = q.next
                    del q
                    counter += 1
                    q = p.next

                r.next = q
                del p
                counter += 1
                p = q

            else:
                r = p
                p = p.next

        self.first = self.first.next
        return counter

lid = linked_list()
lid.insert(1)
lid.insert(1)
lid.insert(1)
lid.insert(2)
lid.insert(3)
lid.insert(4)
lid.insert(4)
lid.insert(5)
lid.printlist()
lid.uniq()
lid.printlist()