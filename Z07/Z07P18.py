#Proszę napisać funkcję, która pozostawia w liście wyłącznie elementy
#unikalne. Do funkcji należy przekazać wskazanie na pierwszy element listy.

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


    def uniq2(self):
        war = node()
        war.next = self.first
        self.first = war

        prev = self.first

        while prev.next:
            curr = prev.next
            dele = False

            while curr.next:

                if prev.next.value == curr.next.value: #jezeli został znaleziony element o takiej samej wartości jak ten na który wskazuje prev
                    dele = True
                    tmp = curr.next
                    curr.next = tmp.next
                    del tmp

                else:
                    curr = curr.next

            if dele: #jezeli zostal znaleziony chociaz jeden taki sam element to kasujemy ten dla ktorego bylo sprawdzane

                tmp = prev.next
                prev.next = tmp.next
                del tmp

            else:
                prev = prev.next

        self.first = self.first.next



    def uniq(self):
        if self.first == None or self.first.next == None:
            return

        prev = node()
        prev.next = self.first

        while prev.next:
            curr = prev.next
            dele = False

            while curr.next:

                if prev.next.value == curr.next.value: #jezeli został znaleziony element o takiej samej wartości jak ten na który wskazuje prev
                    dele = True
                    tmp = curr.next
                    curr.next = tmp.next
                    del tmp

                else:
                    curr = curr.next

            if dele: #jezeli zostal znaleziony chociaz jeden taki sam element to kasujemy ten dla ktorego bylo sprawdzane
                if prev.next == self.first: #w wersji na górze przesuwa sie first przed 'pierwszy' element i nie trzeba tego ifa za kazdym razem sprawdzac
                    self.first = prev.next.next

                tmp = prev.next
                prev.next = tmp.next
                del tmp

            else:
                prev = prev.next

lid = linked_list()
lid.insert(2)
lid.insert(3)
lid.insert(1)
lid.insert(2)
lid.insert(2)
lid.insert(1)
lid.insert(1)
lid.printlist()
lid.uniq2()
lid.printlist()