
 #Tablica t[N] jest wypełniona liczbami naturalnymi. Skok z pola i-tego można wykonać na pola
#o indeksach i+k, gdzie k jest czynnikiem pierwszym liczby t[i] (mniejszym od niej samej). Napisz funkcję,
#która sprawdza, czy da się przejść z pola 0 do N-1 – jeśli się da, zwraca ilość skoków, jeśli się nie da, zwraca
#-1.

from random import randint
import sys

def skoki(t, id, skok):






#t = [1, 1 ,1 ,1 ,1]
#t = [0, 0, 0, 0]
#t = [6, 2, 3, 4, 5, 6]
t = [6, 2, 2 ,6 ,2, 2, 2]
#t = [6, 2, 9, 7, 9, 6, 4, 8, 5, 8]
N = 10
#t = [randint(2, 10) for _ in range(N)]
#print(len(t))
print(skoki(t, 0, 0))

