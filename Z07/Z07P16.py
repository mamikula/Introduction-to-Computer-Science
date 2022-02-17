#Proszę napisać funkcję, która otrzymując jako parametr wskazujący na
#początek listy jednokierunkowej, przenosi na początek listy te z nich,
#które mają parzystą ilość piątek w zapisie ósemkowym.

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

        tmp.next = node(new_val)

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end=" ")
            tmp = tmp.next
        print('\n')

    def transfer(self):
        if self.first == None or self.first.next == None:
            return

        prev = self.first
        while prev.next:
            if fives(prev.next.value):
                curr = prev.next
                prev.next = curr.next
                curr.next = self.first
                self.first = curr
            else:
                prev = prev.next

def fives(num):
    counter = 0
    while num > 0:
        if num % 8 == 5:
            counter += 1
        num //= 8

    if counter % 2 == 0 and counter != 0:
        return True
    return False

lid = linked_list()
lid.insert(1)
lid.insert(45)
lid.insert(10)
lid.insert(15)
lid.insert(23332)
lid.insert(34)
lid.insert(0)
lid.insert(21166)
lid.insert(3)
lid.printlist()
lid.transfer()
lid.printlist()