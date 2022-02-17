#Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000 i sprawdzający
#czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.
N = 10
import random

def parzyste(tab):
    for i in range(0, N):
        zawiera = False
        while tab[i] > 0:
            if (tab[i] % 10) % 2 == 1:
                zawiera = True
                break

            tab[i] //= 10

        if not zawiera:
            return False

    return True



def mian():
    tab = [0]*N
    for i in range(0, N):
        tab[i] = random.randint(1, N)

    if parzyste(tab):
        print(tab)
        print('Tak')
    else:
        print(tab)
        print('Nie')

mian()