#Proszę napisać funkcję, która rozdziela listę na dwie listy. Pierwsza
#powinna zawierać klucze parzyste dodatnie, drugi klucze nieparzyste ujemne,
#pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać
#wskaźniki na listę z danymi oraz wskaźniki na listy wynikowe. Funkcja
#powinna zwrócić liczbę usuniętych elementów.

class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


class linked_list:
    def __init__(self):
        self.first = None


    def insert(self, num):
        if self.first is None:
            self.first = node(num)
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        tmp.next = node(num)


    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end =" ")
            tmp = tmp.next
        print('\n')

    def deleting(self):
        var = node()
        var.next = self.first
        self.first = var
        evenplus = linked_list()
        oddminus = linked_list()
        p = self.first
        cnt = 0

        while p.next:
            if p.next.value > 0 and p.next.value % 2 == 0:
                evenplus.insert(p.next.value)
                p = p.next

            elif p.next.value < 0 and p.next.value % 2 == 1:
                oddminus.insert(p.next.value)
                p = p.next

            else:
                tmp = p.next
                p.next = tmp.next
                del tmp
                cnt += 1


        self.first = self.first.next
        oddminus.printlist()
        evenplus.printlist()


        return cnt

lista = linked_list()
lista.insert(1)
lista.insert(-1)
lista.insert(2)
lista.insert(-3)
lista.insert(-6)
lista.insert(8)
lista.insert(12)
lista.insert(-5)
lista.insert(3)
print(lista.deleting())