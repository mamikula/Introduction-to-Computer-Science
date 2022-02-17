#Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość
#True w przypadku, gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość
#False w przeciwnym przypadku.
import random
N = 4

def zera(t):

    for i in range(N):
        kol = False
        wie = False
        for j in range(N):

            if t[i][j] == 0:
                wie = True

            if t[j][i] == 0:
                kol = True

        if not kol or not wie:
            print("Nie")
            return False
    print('Tak')
    return True






t = [[random.randint(0, 1) ] for _ in range(N)]
#t = [[0, 0, 2, 3], [3, 0, 2, 2], [1, 2, 0, 4], [1, 2, 3, 0]]
zera(t)
for i in t:
    print(i)