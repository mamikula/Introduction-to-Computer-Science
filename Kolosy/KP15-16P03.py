#Dany jest zbiór punktów płaszczyzny o współrzędnych będących liczbami całkowitymi.Zbior
#ten dany jest w postaci listy jednokierunkowej. Proszę funkcję, która rozdziela łańcuch na cztery
#łańcuchy zawierające punkty należące odpowiednio do l,ll,lll i lV ćwiartki układu współrzędnych,
#natomiast punkty leżące na osiach układu współrzędnych usuwa z pamięci. Proszę zadeklarować
#odpowiednie typy.

class node:
    def __init__ (self, value = None, next = None):
        self.value = value
        self.next = next


def insert(list, num):
    if list.value == None:
        list.value = num
        return

    tmp = list
    while tmp.next:
        tmp = tmp.next

    tmp.next = node(num)

def printlist(first):
    tmp = first
    while tmp:
        print(tmp.value, end =" ")
        tmp = tmp.next
    print()

def quarters(f1):
    tmp1 = node()
    tmp1.next = f1
    f1 = tmp1

    p = f1
    c1 = node()
    c2 = node()
    c3 = node()
    c4 = node()

    while p.next:

        if p.next.value[0] > 0 and p.next.value[1] > 0:
            insert(c1, (p.next.value[0], p.next.value[1]))
            p = p.next

        elif p.next.value[0] < 0 and p.next.value[1] > 0:
            insert(c2, (p.next.value[0], p.next.value[1]))
            p = p.next

        elif p.next.value[0] < 0 and p.next.value[1] < 0:
            insert(c3, (p.next.value[0], p.next.value[1]))
            p = p.next

        elif p.next.value[0] > 0 and p.next.value[1] < 0:
            insert(c4, (p.next.value[0], p.next.value[1]))
            p = p.next

        else:
            tmp = p.next
            p.next = tmp.next
            del tmp

    printlist(c1)
    printlist(c2)
    printlist(c3)
    printlist(c4)
    f1 = f1.next
    printlist(f1)


f1 = node()
insert(f1, (1, 1))
insert(f1, (1, 0))
insert(f1, (-1, 1))
insert(f1, (-1, -1))
insert(f1, (1, -1))
insert(f1, (0, 1))

printlist(f1)

quarters(f1)