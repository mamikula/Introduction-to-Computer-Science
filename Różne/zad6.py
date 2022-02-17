#Marcin Mikuła

class node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next


#Zbiór mnogościowy liczb naturalnych reprezentowany jest przez listę o uporządkowanych rosnąco elementach.
# Proszę napisać funkcję iloczyn(z1,z2,z3), która przekształca 3 listy (zbiory) z1,z2,z3 w jedną
#listę (zbiór) zawierającą elementy będące częścią wspólna zbiorów z1,z2,z3. Funkcja powinna zwrócić
#wskazanie do listy wynikowej.

#def dele(before, todel):
    #before.next = todel.next
    #del todel


def iloczyn (z1, z2, z3):
    if z1.val == None or z2.val == None or z3.val == None:
        return node()
    #przesuwam wszystkie pierwsze wskazniki przed pierwsze elementy, zeby z usuwaniem nie bylo problemu
    tmp1 = node()
    tmp1.next = z1
    z1 = tmp1

    tmp2 = node()
    tmp2.next = z2
    z2 = tmp2

    tmp3 = node()
    tmp3.next = z3
    z3 = tmp3

    p = z1
    q = z2
    z = z3

    while p.next and q.next and z.next:
        if p.next.val == q.next.val == z.next.val: # jezeli rowne wartosci to zostawiam
            p = p.next
            q = q.next
            z = z.next

        #jezeli ktoras sie rozni to usuwane sa wszystkie
        elif p.next.val < q.next.val:
            #nie zdążyłem napisać funkcji która by usuwała
            tmp = p.next
            p.next = tmp.next
            del tmp
        elif q.next.val < p.next.val:
            tmp = q.next
            q.next = tmp.next
            del tmp
        elif p.next.val < z.next.val:
            tmp = p.next
            p.next = tmp.next
            del tmp
        elif p.next.val > z.next.val:
            tmp = z.next
            z.next = tmp.next
            del tmp
        elif q.next.val < z.next.val:
            tmp = q.next
            q.next = tmp.next
            del tmp
        elif z.next.val < q.next.val:
            tmp = z.next
            z.next = tmp.next
            del tmp

    if p.next != None:
        while p.next:
            tmp = p.next
            p.next = tmp.next
            del tmp
    #jezeli listy byly roznej dlugosci trzeba sprawdzic czy na koncu nie zostaly jeszcze jakies wartosci
    if q.next != None:
        while q.next:
            tmp = q.next
            q.next = tmp.next
            del tmp

    if z.next != None:
        while z.next:
            tmp = z.next
            z.next = tmp.next
            del tmp

    return z1.next




