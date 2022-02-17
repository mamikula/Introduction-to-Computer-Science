#Proszę napisać funkcję, otrzymującą jako parametr wskaźnik na pierwszy
#element listy o wartościach typu int, usuwającą wszystkie elementy, których
#wartość jest mniejsza od wartości bezpośrednio poprzedzających je
#elementów.


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
            print(tmp.value, end=' ')
            tmp = tmp.next
        print('\n')

    def fun(self):
        if self.first == None or self.first.next == None:
            return

        prev = self.first
        while prev.next:
            if prev.next.value < prev.value:
                curr = prev.next
                prev.next = curr.next
                del curr
            else:
                prev = prev.next


link = linked_list()
link.insert(1)
link.insert(0)
link.insert(3)
link.insert(2)
link.insert(2)
link.insert(1)
link.insert(0)
link.printlist()
link.fun()
link.printlist()