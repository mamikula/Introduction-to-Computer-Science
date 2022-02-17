#Dane są trzy listy jednokierunkowe uporządkowane rosnąco bez powtarzających się
#liczb. Proszę napisać funkcję która usunie w każdej liście elementy powtarzające się
#w trzech listach. Funkcja ma zwrócić liczbę usuniętych elementów.

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

def deleting(s1, s2, s3):
    tmp1 = node()
    tmp1.next = s1
    s1 = tmp1

    tmp2 = node()
    tmp2.next = s2
    s2 = tmp2

    tmp3 = node()
    tmp3.next = s3
    s3 = tmp3

    p = s1
    q = s2
    z = s3
    cnt = 0
    while p.next and q.next and z.next:
        if p.next.value == q.next.value == z.next.value:
            tmp = p.next
            p.next = tmp.next
            del tmp

            tmp = q.next
            q.next = tmp.next
            del tmp

            tmp = z.next
            z.next = tmp.next
            del tmp
            cnt += 3

        elif p.next.value < q.next.value:
            p = p.next
        elif q.next.value < p.next.value:
            q = q.next
        elif p.next.value < z.next.value:
            p = p.next
        elif p.next.value > z.next.value:
            z = z.next
        elif q.next.value < z.next.value:
            q = q.next
        elif z.next.value < q.next.value:
            z = z.next

    f1.first = s1.next
    f2.first = s2.next
    f3.first = s3.next
    return cnt

f1 = linked_list()
f2 = linked_list()
f3 = linked_list()

f1.insert(1)
f1.insert(13)
f1.insert(14)
f1.insert(14)
f1.insert(25)

f2.insert(1)
f2.insert(3)
f2.insert(13)
f2.insert(25)
f2.insert(30)

f3.insert(1)
f3.insert(4)
f3.insert(13)
f3.insert(15)
f3.insert(25)
f3.insert(31)

f1.printlist()
f2.printlist()
f3.printlist()

print(deleting(f1.first, f2.first, f3.first))
f1.printlist()
f2.printlist()
f3.printlist()