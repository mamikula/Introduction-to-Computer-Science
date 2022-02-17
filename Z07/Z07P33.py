#33. Napis s1 poprzedza napis s2 jeżeli ostatnia litera s1 jest „mniejsza”
#od pierwszej litery s2. Według tej zasady rozmieszczono napisy w liście
#cyklicznej, na przykład:
#┌─bartek──leszek──marek──ola──zosia─┐
#└───────────────────────────────────┘
#Proszę napisać stosowne definicje typów oraz funkcję wstawiającą do listy
#napis z zachowaniem zasady poprzedzania. Do funkcji należy przekazać
#wskaźnik do listy oraz wstawiany napis, funkcja powinna zwrócić wartość
#logiczną wskazującą, czy udało się wstawić napis do listy. Po wstawieniu
#elementu wskaźnik do listy powinien wskazywać na nowo wstawiony element.

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

    def makecycle(self):
        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        tmp.next = self.first


    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end =" ")
            tmp = tmp.next
            if tmp == self.first:
                break
        print('\n')

    def possible(self, neword):
        p = self.first
        p = p.next
        makeable = False

        #trzeba dopisac sprawdzenie z pierwszym elementem tym pod self.first

        while p != self.first:
            word = p.value
            ostatniastarego = word[len(word) - 1]    #ostatnia litera poprzedzajacego
            pierwszanowego = neword[0]               #pierwsza litera wstawianego
            ostatnianowego = neword[len(neword) - 1] #
            przednowym = p.next.value
            pierwszaprzednowym = przednowym[0]


            if ostatniastarego < pierwszanowego and ostatnianowego < pierwszaprzednowym:

                tmp = node(neword)
                tmp.next = p.next
                p.next = tmp

                self.first = tmp
                makeable = True
                print(makeable)
                return makeable

            else:
                p = p.next

        print(makeable)
        return makeable

namelist = linked_list()
namelist.insert("abartek")
namelist.insert("leszek")
namelist.insert("amarek")
namelist.insert("aola")
namelist.makecycle()
namelist.possible("zosia")

namelist.printlist()


