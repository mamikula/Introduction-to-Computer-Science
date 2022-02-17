#Napisać program wypełniający N-elementową tablicę t liczbami naturalnymi 1-1000
#i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste

N = 10
import random

def nieparzyste(tab):
    for i in range(0, N):
        zawiera = True
        while tab[i] > 0:
            if (tab[i] % 10) % 2 == 0:
                zawiera = False
                break

            tab[i] //= 10

        if zawiera:
            return True

    return False

def main():

    tab = [0]*N
    for i in range(0, N):
        tab[i] = random.randint(1, N)

    print(tab)
    if nieparzyste(tab):
        print("Tak")
    else:
        print('Nie')

main()