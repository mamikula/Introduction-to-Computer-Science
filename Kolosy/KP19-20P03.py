#Dane są deklarację reprezentujące listę z klockami mag-mina (patrz zadanie 2).
#struct klocek {
 #int a;
 #int b;
 #klocek *next;
#};
#Lista zawiera zestaw klocków, które można ułożyć w ciąg. Niestety klocki pomieszały się. Proszę napisać funkcję,
#która ustawia klocki na liście w ciąg. Uwaga: orientacja klocków w liście jest właściwa.
#Na przykład listę: [2|9] [3|6] [8|2] [2|3] [6|2]
#należy przekształcić na listę: [8|2] [2|3] [3|6] [6|2] [2|9]


class block:
    def __init__(self, left = None, right = None, next = None):
        self.left = left
        self.right = right
        self.next = next

class linked_list:
    def __init__(self):
        self.first = None

    def insert(self, lenu, rinu):
        if self.first == None:
            self.first = block(lenu, rinu)
            return
        tmp = self.first
        while tmp.next:
            tmp = tmp.next
        tmp.next = block(lenu, rinu)

    def printlist(self):
        tmp = self.first
        while tmp:
            print('[',tmp.left, '|', tmp.right, ']', end = "  ")
            tmp = tmp.next
        print()

    def sortmino(self):#głupie to zadanie, za dużo przypadków do sprawdzenia


magmino = linked_list()
magmino.insert(2,9)
magmino.insert(3,6)
magmino.insert(8,2)
magmino.insert(2,3)
magmino.insert(6,2)
magmino.printlist()
#magmino.insert()