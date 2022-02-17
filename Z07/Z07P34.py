#Proszę napisać funkcję, która usuwa z listy cyklicznej elementy,
#których klucz występuje dokładnie k razy. Do funkcji należy przekazać
#wskazanie na jeden z elementów listy, oraz liczbę k, funkcja powinna
#zwrócić informację czy usunięto jakieś elementy z listy.

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

    def printlist (self):
        tmp = self.first
        while tmp:
            print(tmp.value, end = " ")
            tmp = tmp.next
            if tmp == self.first:
                break
        print('\n')

    def makecycle(self):
        tmp = self.first
        while tmp.next:
            tmp = tmp.next

        tmp.next = self.first

    def kcycle(self, k):
        p = self.first
        q = p.next
        ifdel = False
        start = False

        while True:
            if p == self.first and start:
                break
            start = True

            curr = p.value
            cnt = 1
            while q != p:
                if q.value == curr:
                    cnt += 1
                q = q.next
            if cnt == k:
                ifdel = True
                r = p
                while cnt > 0:
                    if r.next.value == curr:
                        if r.next == self.first:
                            self.first = self.first.next
                        tmp = r.next
                        r.next = tmp.next
                        del tmp
                        cnt -= 1
                    else:
                        r = r.next

            p = p.next
            q = p.next
        return ifdel



cycle = linked_list()
cycle.insert(1)
cycle.insert(1)
cycle.insert(2)
cycle.insert(2)
cycle.insert(2)
cycle.insert(3)
cycle.insert(3)
cycle.insert(3)
cycle.insert(2)
cycle.makecycle()
print(cycle.kcycle(3))
cycle.printlist()