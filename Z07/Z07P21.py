#Kolejne elementy listy o zwiększającej się wartości pola val nazywamy
#podlistą rosnącą. Proszę napisać funkcję, która usuwa z listy wejściowej
#najdłuższą podlistę rosnącą. Warunkiem usunięcia jest istnienie w liście
#dokładnie jednej najdłuższej podlisty rosnącej.

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

    def substring(self):
        if self.first == None or self.first.next == None:
            return

        counter = 1
        maxlen = 1
        p = node()
        one = True

        q = self.first
        while q.next:
            if q.value < q.next.value:

                if p == None:
                    p.next = q

                counter += 1
            else:

                if counter > maxlen:
                    maxlen = counter
                    counter = 1
                    one = True

                elif maxlen == counter:
                    p = node()
                    counter = 1
                    one = False

                else:
                    counter = 1

            q = q.next

        if counter > maxlen:
            one = True
            maxlen = counter
        elif counter == maxlen:
            one = False

