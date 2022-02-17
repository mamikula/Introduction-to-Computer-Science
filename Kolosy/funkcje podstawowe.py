'''def nwd(a, b):
    a, b = abs(a), abs(b)
    while b != 0:
        b = a % b
        a = b
    return a

def nww(a, b):
    return (a * b)/nwd(a, b)

def pierwsza(a):
    if a == 1:
        return False
    for i in range(2, int((a**0.5)) + 1):
        if a % i == 0:
            return False
    return True

def mo(w, k):
    if w >= 0 and w < N and k >= 0 and k < N:
        return True
    return False

def palindrom(t):
    for i in range(0, len(t)):
        if t[i] != t[len(t) - i - 1]:
            return False
    return True


def zamiana(liczba, podstawa):
    lista_cyfr = '0123456789ABCDEF'

    zamieniona_liczba = ''

    licznik = 0
    while podstawa ** licznik <= liczba:
         licznik += 1
    licznik -= 1

    while licznik >= 0:
        zamieniona_liczba += lista_cyfr[liczba // (podstawa ** licznik)]
        liczba = liczba % (podstawa ** licznik)
        licznik -= 1
    print(zamieniona_liczba)

zamiana(1415, 2)


############maski binarne##########
def dl_liczby(liczba): # potrzebna do wybierania cyfr z podanej liczby np liczba dlugosc 5 to tak jakby z piecu kratek wybieram cyfry
    licznik = 0
    while liczba > 1:
        liczba //= 10
        licznik += 1

    return licznik

def max_dziesietna(liczba, n): #wszystkie mozliwosci zbioru 4 elementowego
    res = 0
    for i in range(0, n):
        res = res + 2**i

    return res

def dec_to_bin(x): #generuje permutacje zbioru 4 elementowego, binarnego
    res = 1
    while x > 1:
        res = res * 10 + x % 2
        x //= 2

    return res

def reverse(x): #odwraca liczbe
    res = 0
    while x >= 1:
        res = res * 10 + x % 10
        x = x // 10
    return res

def new_liczba_creator(map, liczba, n): #generator liczb wedlug mapy
    res = 0
    for i in range(0, n):
        if map % 10 == 1:
            res = res * 10 + liczba % 10
        liczba = liczba // 10
        map = map // 10
    res = reverse(res)

    return res


### MASKI BITOWE NA STRINGACH
N = 4

for i in range(0,2*N):
    tmp = ''
    for j in range(0,N):
        if (i & 2*j):
            tmp += '1'
        else:
            tmp += '0'
    print(tmp)


#########koniec masek##################

#########wskaźniki####################

#dodawanie elementu do listy na koniec
class node:
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next


def merge(f1, f2): #scalanie 2 list, jedna posortowana druga nie
    tmp1 = node()
    tmp1.next = f1
    f1 = tmp1
    tmp2 = node()
    tmp2.next = f2
    f2 = tmp2

    q = f2

    while q.next:
        p = f1
        tmp = node(q.next.value)
        while p.next != None and p.next.value < q.next.value:
            p = p.next

        if p.next == None:
            p.next = node(q.next.value)

        else:
            tmp.next = p.next
            p.next = tmp

        q = q.next

    f1 = f1.next
    printlist(f1)
    #printlist(f2)
    return f1

def insert(first, num):
    if first.value == None:
        first.value = num
        return
    tmp = first
    while tmp.next:
        tmp = tmp.next

    tmp.next = node(num)

def putfirst(f1, num):
    tmp = node(num)
    tmp.next = f1
    f1 = tmp
    return f1

def putinside(f1, num):
    tmp = f1
    while tmp.next.value < num:
        tmp = tmp.next

    tmp2 = node(num)
    tmp2.next = tmp.next
    tmp.next = tmp2

def printlist(first):
    tmp = first
    while tmp:
        print(tmp.value, end = " ")
        tmp = tmp.next
    print()

def delfirst(f1):
    tmp = f1
    f1 = f1.next
    del tmp
    return f1

def delast(f1):
    tmp = f1
    while tmp.next.next:
        tmp = tmp.next
    del tmp.next
    tmp.next = None



f1 = node()
insert(f1, 1)
insert(f1, 2)
insert(f1, 3)
printlist(f1)
#f1 = putfirst(f1, None)
#f1 = delfirst(f1)
delast(f1)
putinside(f1, 3/2)
printlist(f1)
'''

class Node:
  def __init__(self):
    self.next = None
    self.value = None


def insert_to_node (node, L):
    start = L
    while L.next != None and L.next.value < node.value:
        L = L.next

    node.next = L.next
    L.next = node
    return start


def printList (L):
    if L is not None:
        print(L.value, end = " ")
        printList(L.next)
    else:
        print()


L = Node()
nnode = Node()
nnode.value = 2
L.next = nnode
nn = Node()
nn.value = 5
nnode.next = nn
#printList(L)
a = Node()
a.value = 1
insert_to_node(a, L)
#printList(L)
b = Node()
b.value = 3
insert_to_node(b, L)
#printList(L)
c = Node()
c.value = 7
insert_to_node(c, L)
printList(L)

def reverse(L):
    if L is None or L.next is None:
        return

    prev = None
    curr = L
    nxt = L.next

    while curr:
        curr.next = prev
        prev = curr
        curr = nxt
        if nxt != None:
            nxt = nxt.next

    printList(prev)
    return prev


def reverse2 (L):
    if L is None:
        return

    prev = None

    nxt = L.next

    while L:
        L.next = prev
        prev = L
        L = nxt
        if nxt != None:
            nxt = nxt.next

    printList(prev)
    return prev


reverse2(L)


