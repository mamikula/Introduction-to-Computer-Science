#Zastosowanie listy odsyłaczowej do implementacji
#tablicy rzadkiej. Proszę napisać trzy funkcje:
#– inicjalizującą tablicę,
#– zwracającą wartość elementu o indeksie n,
#– podstawiającą wartość value pod indeks n.


#nie sugerowac sie nazwami zmiennych !!!
class node:
    def __init__ (self, value = None, id = None, next = None):
        self.value = value
        self.id = id
        self.next = next

class chained_list:
    def __init__ (self):
        self.first = None
        self.last = None

    def insert(self, new_val, new_id):
        new = node(new_val, new_id)
        if self.first == None:
            self.last = self.first = new
            return

        tmp = self.first
        while tmp != self.last:
            if tmp.id == new_id: #przy okazji podstawia
                print(tmp.id)
                tmp.value = new_val
                return tmp.value
            tmp = tmp.next

        if self.last.id == new_id:
            self.last.value = new_val

        self.last.next = new
        self.last = new

    def val_to_print(self, new_id):

        if self.last is None:
            return -1
        if self.last.id == new_id:
            return self.last.value

        tmp = self.first
        while tmp != self.last:
            if tmp.id == new_id:
                return tmp.value
            tmp = tmp.next

        return -1

f1 = chained_list()
f1.insert(10, 2)
f1.insert(16, 3)
f1.insert(17, 3)
f1.insert(19, 10000)
f1.insert(18, 5)
print(f1.val_to_print(4))
print(f1.val_to_print(3))
print(f1.val_to_print(10000))