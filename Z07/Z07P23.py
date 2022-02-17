#Dana jest lista, który zakończona jest cyklem.
#Napisać funkcję, która zwraca liczbę elementów w cyklu.

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


    def insert_cycle(self, num):

        tmp = self.first
        while tmp.value != num:
            tmp = tmp.next

        tmp2 = tmp
        while tmp2.next:
            tmp2 = tmp2.next

        tmp2.next = tmp

    def printlist(self):
        tmp = self.first
        while tmp:
            print(tmp.value, end = " ")
            tmp = tmp.next
        print('\n')

    def cycle_length(self):

        p = q = self.first
        while True:
            p = p.next
            q = q.next.next
            if p == q:
                break
        cnt = 0
        while True:
            p = p.next
            q = q.next.next
            cnt += 1
            if p == q:
                break
        return cnt

cycl = linked_list()
cycl.insert(0)
cycl.insert(2)
cycl.insert(3)
cycl.insert(4)
cycl.insert(1)
cycl.insert(1)
cycl.insert(1)
cycl.insert(1)
cycl.insert(1)
cycl.insert_cycle(1)
print(cycl.cycle_length())