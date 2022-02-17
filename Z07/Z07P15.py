#Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
#początek listy jednokierunkowej, usuwa z niej wszystkie elementy, w których
#wartość klucza w zapisie trójkowym ma większą ilość jedynek niż dwójek.



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

    def fun (self):
        if self.first == None:
            return

        while triple(self.first.value):
            tmp = self.first
            self.first = self.first.next
            del tmp

        prev = self.first
        while prev.next:
            if triple(prev.next.value):
                curr = prev.next
                prev.next = curr.next
                del curr
            else:
                prev = prev.next

def triple (a):

    l1 = 0
    l2 = 0
    while a > 0:
        if a % 3 == 1:
            l1 += 1
        elif a % 3 == 2:
            l2 += 1
        a //= 3


    return l1 > l2


link = linked_list()
link.insert(9)
link.insert(9)
link.insert(9)
link.insert(2)
link.insert(2)
link.insert(1)
link.insert(1)
link.printlist()
link.fun()
link.printlist()

