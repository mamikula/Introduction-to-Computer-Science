#Proszę napisać funkcję, która rozdziela elementy listy odsyłaczowej do
#10 list, według ostatniej cyfry pola val. W drugim kroku powstałe listy
#należy połączyć w jedną listę odsyłaczową, która jest posortowana
#niemalejąco według ostatniej cyfry pola val.


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
        while tmp.next != None:
            tmp = tmp.next

        if tmp.next == None:
            tmp.next = node(new_val)

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value)
            tmp = tmp.next

    def separe(self):
        tid = [node()] * 10
        tnd = [node()] * 10
        #print(tnd[1].value)
        tmp = self.first

        while tmp is not None:
            id = tmp.value % 10
            #print(tid[id].value)
            if tid[id].value == None:
                tid[id] = tnd[id].next = tmp
                #print(tid[id].value)
            else:
                tnd[id].next = tmp
                #print(tnd[id].next.value)
            tmp = tmp.next

        #w tym while lista jest rozdzielana do 10 tablic wskazników zgodnie z cyfra jednosci

        result = node()
        last = node()

        for i in range(10):
            if tid[i].value != None:
                if result.value == None:
                    result = tid[i]
                else:
                    last.next = tid[i]
                    last = tnd[i]
                    
        while result:
            print(result.value)
            result = result.next


        self.first = result
        return self.first


f1 = linked_list()
f1.insert(11)
f1.insert(12)
f1.insert(13)
f1.insert(14)
f1.insert(15)
f1.insert(16)
f1.insert(17)
f1.insert(18)
f1.insert(19)
f1.insert(21)
f1.insert(22)
f1.insert(23)
#f1.printlist()
f1.separe()

