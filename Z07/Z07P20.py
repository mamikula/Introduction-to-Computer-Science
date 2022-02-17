#Dana jest lista zawierająca ciąg obustronnie domkniętych przedziałów.
#Krańce przedziałów określa uporządkowana para liczb całkowitych. Proszę
#napisać stosowne deklaracje oraz funkcję redukującą liczbę elementów listy.
#Na przykład lista: [15,19] [2,5] [7,11] [8,12] [5,6] [13,17]
#powinien zostać zredukowany do listy: [13,19] [2,6] [7,12]

class node:
    def __init__(self, l = None, r = None, next = None):
        self.l = l
        self.r = r
        self.next = next

class linked_list:
    def __init__(self):
        self.first = None

    def insert(self, nvl, nvr):
        if self.first == None:
            self.first = node(nvl, nvr)
            return

        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        tmp = node(nvl, nvr)

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.left, tmp.right, end = " ")
            tmp = tmp.next
        print('\n')

    def reduct(self):
        prev = node()
        prev.next = self.first
        while prev.next:
            curr = prev.next
            while curr.next:
                if curr.next.l <= prev.next.l and curr.next.r <= prev.next.r and prev.next.l < curr.next.r:#jezeli nowy lewy wiekszy rowny od starego lewego i stary lewy mniejszy od nowego prawego, i prawy nowy mniejszy lub rowny od starego prawego to zamieniam pierwsze elementy
                    prev.next.l = curr.next.l
                    tmp = curr.next
                    curr.next = tmp.next
                    del tmp



