#Proszę napisać funkcję usuwającą ostatni element listy. Do funkcji
#należy przekazać wskazanie na pierwszy element listy.

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

    def separate(self):
        if self.first == None:
            return

        if self.first.next == None:
            self.first = node()
            return
            #del self.first


        tmp = self.first
        while tmp.next.next:
            tmp = tmp.next

        del tmp.next
        tmp.next = None

start = linked_list()
#start.insert(1)
#start.insert(2)
#start.insert(3)
#start.insert(4)
#start.insert(5)
#start.printlist()
start.separate()
start.printlist()