#Dany jest ciąg zer i jedynek zapisany w tablicy T[N]. Proszę napisać funkcję, która odpowiada
#na pytanie czy jest możliwe pocięcie ciągu na kawałki z których każdy reprezentuje liczbę pierwszą. Długość
#każdego z kawałków nie może przekraczać 30. Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu
#110100 nie jest możliwe.

from random import randint

def pierwsza(a):
    if a < 2:
        return False
    for i in range(2, a):
        if a % i == 0:
            return False
    return True


def kawalki(tab, id):

    if id == len(tab):
        return True
    a = 0
    for i in range(id, len(tab)):
        if i > 30 + id:
            return False

        a = a * 2 + tab[i]  #zamiana ciagu binarnego na liczbe dziesietna
        if pierwsza(a) and kawalki(tab, i + 1):
            print(a)
            return True

    return False


def main():
    N = 31
    #t = [1, 1, 0, 1, 0, 0]
    t = [1, 1, 1, 1, 1]
    #t = [0, 0, 0, 0, 0, 0]
    #t = [randint(0, 1) for _ in range(N)]
    #print(t)
    #t = [1, 1, 1, 1, 1, 1, 1]
    print(kawalki(t, 0))
main()