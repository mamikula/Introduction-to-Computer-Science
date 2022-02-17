#Proszę napisać funkcję wstawiającą na koniec listy nowy element. Do
#funkcji należy przekazać wskazanie na pierwszy element listy oraz wstawianą
#wartość.

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

def add_new(start, new_val):
    if start == None:
        start = node(new_val)

    tmp = start
    while tmp.next:
        tmp = tmp.next

    tmp.next = node(new_val)
    print(tmp.value)
    print(tmp.next.value)

f1 = linked_list()
f1.insert(11)
add_new(f1.first, 10)